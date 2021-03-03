from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(250), nullable=False, unique=True)
    gender = db.Column(db.String(250), nullable=False)
    rel = relationship('Favoritos')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name" : self.name,
            "gender" : self.gender,
            # do not serialize the password, its a security breach
        }
class Personaje(db.Model):
    _tablename_ = "personajes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    height = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(200), nullable=False, unique=False)
    hair_color= db.Column(db.String(200), nullable=False)
    eye_color= db.Column(db.String(250), nullable=False)
    rel = relationship('Favoritos')
        
    def _repr_(self):
        return '<User %r>' % self.username
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }
class Planetas(db.Model) :
    _tablename_ = "planetas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    diameter = db.Column(db.String(300), nullable=False)
    rotation_period = db.Column(db.String(300), nullable=False)
    gravity = db.Column(db.String(300), nullable=False)
    population= db.Column(db.String(300), nullable=False)
    climate = db.Column(db.String(200), nullable=False) 
    rel = relationship('Favoritos')

    def _repr_(self):
        return {
    
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
        }
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "climate": self.climate
        }
class Favoritos(db.Model):
    _tablename_= 'favoritos'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    personajes_name =db.Column(db.String(250),ForeignKey('personaje.name'))
    planetas_name = db.Column(db.String(250),ForeignKey('planetas.name'))
    user_name = db.Column(db.String(250),ForeignKey('user.name'))
    
    
    def _repr_(self):
        return '<User %r' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "Personaje_name" : self.Personaje_name,
            "planetas_name": self.planetas_name,
            "user_name" : self.user_name
        }