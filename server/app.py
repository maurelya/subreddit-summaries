#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, session
from database import add_user_record, Users


app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print(data)
    #new_user = Users()
    #add_user_record(new_user)