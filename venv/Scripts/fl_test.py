import json
import user.json

j = json.loads(user.json)
print(j['users'])
