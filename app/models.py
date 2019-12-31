from datetime import datetime
from app import db

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    address_street = db.Column(db.String(64))
    address_city = db.Column(db.String(32))
    address_postcode = db.Column(db.String(16))
    email = db.Column(db.String(120), index=True)
    mobile = db.Column(db.String(120), index=True)
    deleted = db.Column(db.Boolean(), default=False)
    added_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Member {} {} {}>'.format(self.name, self.address_street, self.deleted) 