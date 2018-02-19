# This module uses Twitter API to get information about user's followers
# The information about them is written to the file 'followers.json'
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def get_json(account):
    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': account, 'count': '20'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    with open("followers.json", 'w') as f:
        print(json.dumps(js, indent=2), file=f)
