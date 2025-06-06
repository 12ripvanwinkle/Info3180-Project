from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    description = db.Column(db.String(255))
    parish = db.Column(db.String(100))
    biography = db.Column(db.Text)
    sex = db.Column(db.String(20))
    race = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    height = db.Column(db.String(10))
    fav_cuisine = db.Column(db.String(100))
    fav_colour = db.Column(db.String(50))
    fav_school_subject = db.Column(db.String(100))
    political = db.Column(db.Boolean)
    religious = db.Column(db.Boolean)
    family_oriented = db.Column(db.Boolean)

    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    def __repr__(self):
        return f"<Profile of user_id={self.user_id_fk}>"


class Favourite(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id_fk], backref='favourites_given')
    fav_user = db.relationship('User', foreign_keys=[fav_user_id_fk], backref='favourites_received')

    def __repr__(self):
        return f"<Favourite: user {self.user_id_fk} ➜ user {self.fav_user_id_fk}>"
