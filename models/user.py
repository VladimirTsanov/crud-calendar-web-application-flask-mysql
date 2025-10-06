from extensions import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tasks= db.relationship('Task', backref='author', lazy=True)
    events=db.relationship('Event', backref='author', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.username