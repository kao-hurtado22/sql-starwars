import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)
    world = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    relacion = relationship ('favorites_characters')

class planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    world = Column(String(250), nullable=False)
    lenguage = Column(String(250), nullable=False)
    relacion = relationship ('favorites_planets')


class starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    models = Column(String(250), nullable=False)
    relacion = relationship ('favorites_starships')

class favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class favorites_starships(Base):
    __tablename__ = 'favorites_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')