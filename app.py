from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hi go to the next page <a href= "/hello"> hello</a>'
@app.route('/hello')
def hello():
    return 'Hello'
@app.route('/user/<name>')
def user(name):
    return 'Hello {}!'.format(name)