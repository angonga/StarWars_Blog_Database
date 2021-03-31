import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
#    # Here we define columns for the table address.
#    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)

class Favorites(Base):
   __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('user.id'))
   characters_id = Column(Integer, ForeignKey('characters.id'))
   planets_id = Column(Integer, ForeignKey('planets.id'))

class Characters(Base):
   __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   id = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   birth_year = Column(String(250), nullable=False)
   gender = Column(String(250), nullable=False)
   height = Column(Integer, nullable=False)
   skin_color = Column(String(250), nullable=False)
   hair_color = Column(String(250), nullable=False)
   eye_color = Column(String(250), nullable=False)
   like = relationship(Favorites)

class Planets(Base):
   __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   id = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   climate = Column(String(250), nullable=False)
   population = Column(Integer, nullable=False)
   orbital_period = Column(Integer, nullable=False)
   rotation_period = Column(Integer, nullable=False)
   diameter = Column(Integer, nullable=False)
   terrain = Column(String(250), nullable=False)
   like = relationship(Favorites)

class User(Base):
   __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   id = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   email = Column(String(250), nullable=False)
   password = Column(String(250), nullable=False)
   like = relationship(Favorites)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')