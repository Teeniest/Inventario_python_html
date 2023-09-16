from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True,), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firs_name = db.Column(db.String(50))
    notes = db.relationship('Note')
    productos = db.relationship('Productos')

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(1000))
    precio_anterior = db.Column(db.Float)
    precio_minimo = db.Column(db.Float)
    caducidad = db.Column(db.String(20))
    categoria = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

