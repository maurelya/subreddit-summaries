#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/home', methods=['GET'])
def greetings():
    return jsonify("Hello World")