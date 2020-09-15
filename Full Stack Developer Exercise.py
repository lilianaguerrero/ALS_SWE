from flask import Flask, jsonify, request
import json, requests


app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    users = "http://faker.hook.io/?property=helpers.userCard&amp;locale=en_US"
    user_cards = []
    for i in range(25):
        raw_user = requests.get(users)
        raw_user = raw_user.json()
        user_cards.append(raw_user)
    print(user_cards)
    return "complete: printed user cards to terminal"
    """NOTE: if returning user cards is preferred instead of printing, 
                run: return str(user_cards)"""


if __name__ == ("__main__"):
    app.run(debug=True, port=5000, host="0.0.0.0")