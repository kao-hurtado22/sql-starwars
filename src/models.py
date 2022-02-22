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
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)
    world = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    world = Column(String(250), nullable=False)
    lenguage = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'Starship'
    id = Column(Integer, primary_key=True)
    models = Column(String(250), nullable=False)

class Favorites_Characters(Base):
    __tablename__ = 'Favorites Characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class Favorites_Planets(Base):
    __tablename__ = 'Favorites Planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class Favorites_Starships(Base):
    __tablename__ = 'Favorites startships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')