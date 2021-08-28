import time
from steam.client import SteamClient
from steam.client.builtins.friends import SteamFriendlist

from accounts_parser import get_accounts_data, get_friends_steam_ids

steam_client = SteamClient()

users_data = get_accounts_data()
steam_ids_chunks = get_friends_steam_ids()


@steam_client.on(steam_client.EVENT_AUTH_CODE_REQUIRED)
def steam_user_login(username, password, is_2fa):
    if is_2fa:
        code = input("Enter 2FA Code: ")
        steam_client.login(username, password, two_factor_code=code)
    else:
        code = input("Enter Email Code: ")
        steam_client.login(username, password, auth_code=code)


def friends_adding():
    i = 0
    for user in users_data["accounts"]:
        print(f"logging in account {user['login']}")
        time.sleep(3)
        steam_user_login(user["login"], user["password"], user["2fa"])
        print(f"{steam_client.user.name} friends number {steam_client.friends} --- Before adding")
        for steam_id in steam_ids_chunks[i]:
            print(f"adding friend {steam_id} to {steam_client.user.name} account")
            friends_adder = SteamFriendlist(steam_client)
            print(friends_adder.add(int(steam_id)))
            time.sleep(3)
        i += 1
        time.sleep(3)
        print(f"{steam_client.user.name} friends number {steam_client.friends} --- After adding")
        print(f"logging out account {user}")
        steam_client.logout()


if __name__ == '__main__':
    friends_adding()
