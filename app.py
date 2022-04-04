from datetime import datetime
from http.client import HTTPResponse
from xmlrpc.client import DateTime
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello'
@app.route('/<name>')
def user(name):
    return 'Hello {}!'.format(name)
