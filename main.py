import time
from steam.client import SteamClient
from steam.client.builtins.friends import SteamFriendlist
from steam.webauth import MobileWebAuth
from steam.guard import SteamAuthenticator
from steam import guard

from accounts_parser import get_accounts_data, get_friends_steam_ids

steam_client = SteamClient()

users_data = get_accounts_data()
steam_ids_chunks = get_friends_steam_ids()


def friends_adding():
    i = 0
    for user in users_data["accounts"]:
        print(f"logging in account {user['login']}")
        time.sleep(3)
        steam_client.login(user['login'], user['password'], two_factor_code=get_2FA_code(user))
        for steam_id in steam_ids_chunks[i]:
            print(f"adding friend {steam_id} to {user['login']} account")
            friends_adder = SteamFriendlist(steam_client)
            time.sleep(1)
            friends_adder.add(int(steam_id))
        i += 1
        time.sleep(3)
        print(f"logging out account {user['login']}")
        steam_client.logout()


def friend_list_checking():
    for user in users_data["accounts"]:
        print(f"logging in account {user['login']}")
        time.sleep(3)
        steam_client.login(user['login'], user['password'], two_factor_code=get_2FA_code(user))
        print(f"{user['login']} friends number {steam_client.friends}")

        print(f"logging out account {user['login']}")
        steam_client.logout()


def get_2FA_code(user):
    secret = {'shared_secret': user["shared_secret"], 'identity_secret': user["identity_secret"]}
    steam_authenticator = guard.SteamAuthenticator(secret)
    code = steam_authenticator.get_code()
    return code

if __name__ == '__main__':
    # friends_adding()
    friend_list_checking()
