from flask import Flask, render_template, request
from json_parse import get_users_data, get_user_info
from followers_map import get_locations_dict, create_map
from get_twitter_user import get_json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Followers', methods=['GET','POST'])
def get_account():
    """
    Main function that processes given account name and returns followers map
    """
    account = request.form['account']
    if account == "":
        return render_template("failure.html")
    else:
        get_json(account)
        users = get_users_data('followers.json')
        data = get_user_info(users, 'name', 'location', 'profile_image_url')
        locations = get_locations_dict(data)
        create_map(data, locations)
        return render_template('Followers.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
