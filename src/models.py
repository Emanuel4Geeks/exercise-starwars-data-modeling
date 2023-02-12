import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    relationship('Favoritos', backref='usuario', lazy=True)


class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table personaje.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    altura = Column(Integer, nullable=False)
    peso = Column(Integer, nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    genero = Column(String(50), nullable=False)
    planeta_origen_id = Column(
        Integer, ForeignKey('planeta.id'), nullable=False)
    relationship('Favoritos', backref='personaje', lazy=True)

    def to_dict(self):
        return {}


class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table planeta.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    diametro = Column(Integer, nullable=False)
    clima = Column(String(100), nullable=False)
    terreno = Column(String(100), nullable=False)
    gravedad = Column(String(100), nullable=False)
    poblacion = Column(Integer, nullable=False)
    relationship('Favoritos', backref='planeta', lazy=True)
    relationship('Personaje', backref='planeta', lazy=True)

    def to_dict(self):
        return {}


class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
