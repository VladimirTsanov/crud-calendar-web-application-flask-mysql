from extensions import db
from datetime import datetime

class Event(db.Model):
    __tablename__= 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    datetime_start = db.Column(db.DateTime, nullable=False)
    datetime_end = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(350))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return '<Event %r>' % self.title
        
        
    