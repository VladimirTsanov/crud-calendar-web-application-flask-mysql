from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Pageeeee'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'