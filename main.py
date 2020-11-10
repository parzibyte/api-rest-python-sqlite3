"""
    API REST con Python 3 y SQLite 3
    By Parzibyte: 
    ** https://parzibyte.me/blog **
"""
from flask import Flask, jsonify, request
import game_controller
from db import create_tables

app = Flask(__name__)


@app.route('/games', methods=["GET"])
def get_games():
    games = game_controller.get_games()
    return jsonify(games)


@app.route("/game", methods=["POST"])
def insert_game():
    game_details = request.get_json()
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.insert_game(name, price, rate)
    return jsonify(result)


@app.route("/game", methods=["PUT"])
def update_game():
    game_details = request.get_json()
    id = game_details["id"]
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.update_game(id, name, price, rate)
    return jsonify(result)


@app.route("/game/<id>", methods=["DELETE"])
def delete_game(id):
    result = game_controller.delete_game(id)
    return jsonify(result)


@app.route("/game/<id>", methods=["GET"])
def get_game_by_id(id):
    game = game_controller.get_by_id(id)
    return jsonify(game)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
