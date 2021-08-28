
def get_accounts_data():
    users_data = {"accounts":
                      []
                  }
    steam_ids_txt = open("steam_accounts.txt", "r")
    lines = steam_ids_txt.readlines()
    for line in lines:
        login, password = line.split()
        users_data["accounts"].append({"login": login,
                                       "password": password,
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
