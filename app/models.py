from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from flask_login import UserMixin, login_required

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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