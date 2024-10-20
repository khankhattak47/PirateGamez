from extensions import db  # assuming you've moved db to extensions.py
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(150), primary_key=True)  # Assuming username is the primary key
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
