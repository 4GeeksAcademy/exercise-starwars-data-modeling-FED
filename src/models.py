import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    bio = Column(String(500))  # Additional attribute: user biography or description

    # Relationships
    favorites = relationship('Favorite', back_populates='user')
    posts = relationship('Post', back_populates='author')  # Example: User posts relationship

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    height = Column(Integer)
    birth_year = Column(String(50))
    image_url = Column(String(250))  # Additional attribute: character image URL

    # Relationships
    favorites = relationship('Favorite', back_populates='character')
    appearances = relationship('Appearance', back_populates='character')  # Example: Character appearances

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    image_url = Column(String(250))  # Additional attribute: planet image URL

    # Relationships
    favorites = relationship('Favorite', back_populates='planet')
    appearances = relationship('Appearance', back_populates='planet')  # Example: Planet appearances

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    image_url = Column(String(250))  # Additional attribute: vehicle image URL

    # Relationships
    favorites = relationship('Favorite', back_populates='vehicle')
    appearances = relationship('Appearance', back_populates='vehicle')  # Example: Vehicle appearances

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    created_at = Column(DateTime, default=datetime.now)

    # Relationships
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    vehicle = relationship('Vehicle', back_populates='favorites')

class Appearance(Base):
    __tablename__ = 'appearance'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    # Relationships
    character = relationship('Character', back_populates='appearances')
    planet = relationship('Planet', back_populates='appearances')
    vehicle = relationship('Vehicle', back_populates='appearances')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
