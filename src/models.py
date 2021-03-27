import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Define the structure of the people table
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birth_year = Column(Integer)
    gender = Column(String(30))
    created = Column(String(30))
    edited = Column(String(30))
    homeworld = Column(String(30))
    description = Column(String(30))
    url = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'
    # Define the structure of the planets table
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(30))
    population = Column(Integer)
    climate = Column(String(30))
    terrain = Column(String(30))
    surface_water = Column(String(30))
    created = Column(String(30))
    edited = Column(String(30))
    url = Column(String(50))
    description = Column(String(30))

class Starships(Base):
    __tablename__ = 'starships'
    # Define the structure of the starships table
    id = Column(Integer, primary_key = True)
    model = Column(String(30))
    starship_class = Column(String(30))
    manufacturer = Column(String(30))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    mglt = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(30))
    url = Column(String(50))
    description = Column(String(30))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    object_Type = Column(String(15))
    object_Id = Column(String(50))

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'user'
    # Define the structure of the user table
    id = Column(Integer, primary_key = True)
    user_name = Column(String(30), nullable=False)
    pswd = Column(String(30), nullable=False)
    favorites = relationship(Favorites)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')