def get_accounts_data():
    users_data = {"accounts":
                      []
                  }
    steam_ids_txt = open("steam_accounts.txt", "r")
    lines = steam_ids_txt.readlines()
    for line in lines:
        login, password, shared_secret, identity_secret = line.split()
        users_data["accounts"].append({"login": login,
                                       "password": password,
                                       "shared_secret": shared_secret,
                                       "identity_secret": identity_secret,
                                       "2fa": True})
    return users_data


def get_friends_steam_ids():
    steam_ids = []
    steam_ids_txt = open("steamids.txt", "r")
    lines = steam_ids_txt.readlines()
    for line in lines:
        steam_ids.append(line.rstrip('\n'))

    return list(chunks(steam_ids, 30))


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == '__main__':
    data = get_accounts_data()
    for user in data["accounts"]:
        print(user["login"])
        print(user["password"])
        print(user["shared_secret"])
        print(user["identity_secret"])
        print(user["2fa"])

    steam_ids = get_friends_steam_ids()
    for steam_ids_chunks in steam_ids:
        print(len(steam_ids_chunks))
