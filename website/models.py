from . import db
# from flask_login import UserMixin #para manejo de usuarios
from sqlalchemy.sql import func

from datetime import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy


def generate_uuid():
    return str(uuid.uuid4())


# Admin Model
class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid) 
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False) 
    name = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# User Model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid) #!!convertir este id en secuencial(el primero 1 el segundo 2...)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    has_logged_in = db.Column(db.Boolean, default=False, nullable=False) #!!poner true para cuando se logeen por primera vez 
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Services Model
class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Appointment Model
class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.String(36), db.ForeignKey('services.id'), nullable=False)
    tip = db.Column(db.Float, nullable=True, default=0.0)
    name = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('appointments', lazy=True))
    service = db.relationship('Service', backref=db.backref('appointments', lazy=True))
