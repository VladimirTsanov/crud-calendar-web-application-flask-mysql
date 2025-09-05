from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def index():
    return render_template("login.html")

@app.route('/register')
def hello():
    return render_template("registration.html")

@app.route('/new-post')
def add_post():
    return render_template("add_post.html")

@app.route('/edit-post')
def edit_post():
    return render_template("edit_post.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()