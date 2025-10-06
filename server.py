import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from extensions import db
from markupsafe import escape
from datetime import datetime
from models.user import User
from models.tasks import Task
from models.events import Event
app = Flask(__name__)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), './.envCalendar/.env'))

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()
        print("✅ Таблиците са създадени в базата данни")
    app.run(debug=True)


