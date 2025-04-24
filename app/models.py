# Database schema

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Model for user is below
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(120), nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
    
# Model for profile is below
class profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    parish = db.Column(db.String(100), nullable=True)
    biography = db.Column(db.String(700), nullable=True)
    sex = db.Column(db.String(10), nullable=True)
    race = db.Column(db.String(50), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Float, nullable=True)
    fav_cuisine  = db.Column(db.String(100), nullable=True)
    fav_color = db.Column(db.String(50), nullable=True)
    fav_school_subject = db.Column(db.String(100), nullable=True)
    political = db.Column(db.Boolean, nullable=True)
    religious = db.Column(db.Boolean, nullable=True)
    family_oriented = db.Column(db.Boolean, nullable=True)

    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    def __repr__(self):
        return f"<Profile of {self.user.username}>"
    
# Model for favorites is below
class favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id_fk], backref='favourites_given')
    fav_user = db.relationship('User', foreign_keys=[fav_user_id_fk], backref='favourites_received')

    def __repr__(self):
        return f"<{self.user.username} favorited {self.fav_user.username}>"
