# only concerned with routing and HTTP request/response handling, e.g.

# from flask import Flask, jsonify, request
# from .controller import GameController

# app = Flask(__name__)
# game_controller = GameController()

# @app.route('/start', methods=['POST'])
# def start_game():
#     response = game_controller.start_game()
#     return jsonify(response)

# @app.route('/play/<int:player_number>', methods=['POST'])
# def play_turn(player_number):
#     response = game_controller.play_turn(player_number)
#     return jsonify(response)
