# This module is used to parse json file returned by Twitter API
# in order to get users' information by the given keys
import json


def get_users_data(file_path, n=50, key='users'):
    """
    Function, to get list of dictionaies from the json
    :param n: the quantity of the followers
    :param key: by default used to get users section from json
    :return: the list of dictionaries about users
    """
    json_data = open(file_path).read()
    data = json.loads(json_data)
    users = []
    for i in range(n):
        users.append(data.get(key)[i])
    return users


def get_user_info(users, *keys):
    """
    :param users: list of dictionaries returned by get_users_data()
    :param keys: keywords (e.g. 'screen_name')
    :return: the list of users dictionaries by given keys
    """
    res = []
    for i in range(len(users)):
        info = {}
        for key in keys:
            info.update({key: users[i][key]})
        res.append(info)
    return res
