import json


def get_data_dict(file_path, key):
    json_data = open(file_path).read()
    data = json.loads(json_data)
    return data.get(key)[0]


def get_info(user, *keys):
    info = []
    for key in keys:
        info.append((key, user[key]))
    return info


user = get_data_dict('user.json', 'users')
print(get_info(user, 'name', 'location', 'profile_image_url'))
