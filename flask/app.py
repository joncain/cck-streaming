import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/on_publish', methods=['POST'])
def on_publish():
    key = os.getenv('STREAMKEY')

    if key is None:
      return 'Key could not be found', 500

    if request.form['name'] == key:
        return 'Authenticated', 200

    return 'Authentication failed', 403

