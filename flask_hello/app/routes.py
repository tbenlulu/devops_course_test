from flask import request
from app import app

@app.route('/')
def index():
    return "Index page"

@app.route('/hello')
def hello():
    return "Hello, World!"

