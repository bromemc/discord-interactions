import os

from flask import Flask, jsonify, request
from enum import Enum

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

CLIENT_PUBLIC_KEY = "cc8d90dfdb6b3efa4fbd586a23682c69e1463f856313e3e2f62ddd55cb72402a"

app = Flask(__name__)


class Flags(Enum):
    NONE = 0
    ADMIN_POWER = 1 << 0
    MOD_POWER = 1 << 1
    MFA_REQUIRED = 1 << 2
    HOST_BAN = 1 << 3
    TRAINEE = 1 << 4
    ONBOARDING = 1 << 5
    DISCOURAGE_USER = 1 << 6
    MFA_ENABLED = 1 << 7


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        command_id = request.json['data']['id']
        if command_id == "791069362114265108":  # trello
            return jsonify({
                'type': InteractionResponseType.CHANNEL_MESSAGE,
                'data': {
                    'content': 'https://trello.com/b/LwtOpeci/bromemc',
                    'flags': 64
                }
            })
        if command_id == "791434396024307712" and request.json['data']['options'][0]["name"] == "flag":
            flags_int = request.json['data']['options'][0]["options"][0]["value"]
            str_flags = []
            # (getFlagsAsInteger() & flagEnum.getValue()) == flagEnum.getValue()
            for flag in Flags:
                if (flags_int & flag.value()) == flag.value():
                    str_flags.append(str(flag))

            print(str_flags)
            return jsonify({
                'type': InteractionResponseType.CHANNEL_MESSAGE,
                'data': {
                    'content': '{}'.format(', '.join(str_flags)),
                    'flags': 64
                }
            })


@app.route('/')
def root():
    return jsonify({'message': "The maze wasn't meant for you."})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
