import os

from flask import Flask, jsonify, request

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

CLIENT_PUBLIC_KEY = "cc8d90dfdb6b3efa4fbd586a23682c69e1463f856313e3e2f62ddd55cb72402a"

app = Flask(__name__)


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        command_id = request.json['data']['id']
        if command_id == "791069362114265108": # trello
            return jsonify({
                'type': InteractionResponseType.CHANNEL_MESSAGE,
                'data': {
                    'content': 'https://trello.com/b/LwtOpeci/bromemc',
                    'flags': 64
                }
            })
        if command_id == "791434396024307712":
            return jsonify({
                'type': InteractionResponseType.CHANNEL_MESSAGE,
                'data': {
                    'content': f'yes',
                    'flags': 64
                }
            })



@app.route('/')
def root():
    return jsonify({'message': "The maze wasn't meant for you."})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
