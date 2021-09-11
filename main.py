from steam.client import SteamClient
from steam.client.builtins.friends import SteamFriendlist
from steam import guard
import gevent
import csv

from accounts_parser import get_accounts_data, get_friends_steam_ids

steam_client = SteamClient()

users_data = get_accounts_data()
steam_ids_chunks = get_friends_steam_ids()


def friends_adding():
    i = 0
    for user in users_data["accounts"]:
        steam_client.login(user['login'], user['password'], two_factor_code=get_2fa_code(user))
        print(f'---- {steam_client.friends} \n {user["login"]} --- {len(steam_ids_chunks[i])} --- {steam_ids_chunks[i]}')
        for steam_id in steam_ids_chunks[i]:
            friends_adder = SteamFriendlist(steam_client, logger_name='SteamFriendList')
            friends_adder.add(int(steam_id))
        i += 1
        steam_client.logout()


def friend_list_checking():
    header = ['nickname', 'friends_count']
    rows = []
    for user in users_data["accounts"]:
        print(f"logging in account {user['login']}")
        gevent.sleep(2)
        steam_client.login(user['login'], user['password'], two_factor_code=get_2fa_code(user))
        print(f"{user['login']} friends number {steam_client.friends}")
        rows.append({
            "nickname": user['login'],
            "friends_count": str(steam_client.friends).split()[1]
        })
        print(f"logging out account {user['login']}")
        steam_client.logout()

    print(rows)
    with open('accounts_friends_counter.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def get_2fa_code(user):
    secret = {'shared_secret': user["shared_secret"], 'identity_secret': user["identity_secret"]}
    steam_authenticator = guard.SteamAuthenticator(secret)
    code = steam_authenticator.get_code()
    return code


if __name__ == '__main__':
    friends_adding()
    # friend_list_checking()
