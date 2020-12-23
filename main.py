import os

from flask import Flask, jsonify

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

CLIENT_PUBLIC_KEY = "cc8d90dfdb6b3efa4fbd586a23682c69e1463f856313e3e2f62ddd55cb72402a"

app = Flask(__name__)


@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
    print(request.json)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
