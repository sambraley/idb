#!/usr/bin/env python3
# pylint: disable = invalid-name
# pylint: disable = import-error
# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments

"""
This module is designed to model galaxies, stars, planets, and satellites for
use in a PostgreSQL database using Flask-SQLAlchemy.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Satellite(db.Model):

    """
    Models artificial satellites. Attributes are: name, agency, mission type,
    and year launched. They may relate many-to-one to galaxies, stars, and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    name = db.Column(db.String(), unique=True)
    image = db.Column(db.String())
    year_launched = db.Column(db.Integer)
    mission_type = db.Column(db.String())
    info_url = db.Column(db.String())
    agency = db.Column(db.String())

    # Foreign Keys
    planet_pid = db.Column(db.Integer, db.ForeignKey('planet.pid'))
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # Relations
    planet = db.relationship(
        "Planet", backref=db.backref("satellites", lazy="dynamic"))
    star = db.relationship(
        "Star", backref=db.backref("satellites", lazy="dynamic"))
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("satellites", lazy="dynamic"))

    #
    # Methods
    #

    def __init__(
            self, name, image, year_launched, mission_type, info_url, agency,
            planet, star, galaxy):
        """
        name a str, agency a str, mission_type a str, year_launched an int.
        """
        # Check types
        assert isinstance(image, str)
        assert isinstance(year_launched, int)
        assert isinstance(name, str)
        assert isinstance(mission_type, str)
        assert isinstance(info_url, str)
        assert isinstance(agency, str)
        assert isinstance(planet, Planet)
        assert isinstance(star, Star)
        assert isinstance(galaxy, Galaxy)

        # Create instance
        self.name = name
        self.image = image
        self.year_launched = year_launched
        self.mission_type = mission_type
        self.info_url = info_url
        self.agency = agency
        self.planet = planet
        self.star = star
        self.galaxy = galaxy

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "image": self.image,
            "year_launched": self.year_launched,
            "mission_type": self.mission_type,
            "info_url": self.info_url,
            "agency": self.agency,
            "planet_pid": self.planet_pid,
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Satellite %r>" % self.name

    def serializer(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "image": self.image,
            "year_launched": self.year_launched,
            "type": self.mission_type,
            "info_url": self.info_url,
            "agency": self.agency,
            "planet_pid": self.planet_pid,
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid
        }


class Planet(db.Model):

    """
    Models planets. Attributes are: name, image, diameter, right_ascension,
    declination, gravity, orbital period, mass, and temperature. They may relate
    many-to-one to galaxies and stars, and one-to-many to satellites and other planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    name = db.Column(db.String(), unique=True)
    diameter = db.Column(db.Float)
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    gravity = db.Column(db.Float)
    orbital_period = db.Column(db.Float)
    mass = db.Column(db.Float)
    temperature = db.Column(db.Integer)

    # Foreign Keys
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # Relations
    star = db.relationship(
        "Star", backref=db.backref("planets", lazy="dynamic"))
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("planets", lazy="dynamic"))

    #
    # Methods
    #

    def __init__(
            self, name, diameter, ra, dec, gravity, orbital_period, mass,
            temperature, star, galaxy):
        """
        name a str, image a str, diameter, temperature, right_ascension, declination,
        mass, gravity, orbital_period are all floats.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(diameter, float)
        assert isinstance(ra, float)
        assert isinstance(dec, float)
        assert isinstance(gravity, float)
        assert isinstance(orbital_period, float)
        assert isinstance(mass, float)
        assert isinstance(temperature, int)

        # Create Instance
        self.name = name
        self.diameter = diameter
        self.ra = ra
        self.dec = dec
        self.gravity = gravity
        self.orbital_period = orbital_period
        self.mass = mass
        self.temperature = temperature
        self.star = star
        self.galaxy = galaxy

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "diameter": self.diameter,
            "ra": self.ra,
            "dec": self.dec,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "mass": self.mass,
            "temperature": self.temperature,
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Planet %r>" % self.name


class Star(db.Model):

    """
    Models stars. Attributes are: name, image, temperature, right_ascension,
    declination, and mass. They may relate many-to-one to galaxies and one-to-many
    to satellites and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    name = db.Column(db.String(), unique=True)
    diameter = db.Column(db.Float)
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    temperature = db.Column(db.Integer)
    mass = db.Column(db.Float)

    # Foreign Keys
    galaxy_pid = db.Column(db.Integer, db.ForeignKey("galaxy.pid"))

    # Relations
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("stars", lazy='dynamic'))

    #
    # Methods
    #

    def __init__(self, name, diameter, ra, dec, temperature, mass, galaxy):
        """
        name a str, image a str, temperature, right_ascension, declination, and mass
        are all floats.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(diameter, float)
        assert isinstance(ra, float)
        assert isinstance(dec, float)
        assert isinstance(temperature, int)
        assert isinstance(mass, float)
        assert isinstance(galaxy, Galaxy)

        # Create instance
        self.name = name
        self.diameter = diameter
        self.ra = ra
        self.dec = dec
        self.temperature = temperature
        self.mass = mass
        self.galaxy = galaxy

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "diameter": self.diameter,
            "ra": self.ra,
            "dec": self.dec,
            "temperature": self.temperature,
            "mass": self.mass,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Star %r>" % self.name


class Galaxy(db.Model):

    """
    Models galaxies. Attributes are: name, image, right_ascension, declination,
    galaxy type (spiral, etc), redshift, and angular size. They may relate one-to-many
    to satellites, stars, and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    name = db.Column(db.String(), unique=True)
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    morph_type = db.Column(db.String())
    redshift = db.Column(db.Float)
    size = db.Column(db.Float)

    #
    # Methods
    #

    def __init__(self, name, ra, dec, morph_type, redshift, size):
        """
        name a str, image a str, right_ascension and declination floats, galaxy_type a str,
        redshift and size floats.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(ra, float)
        assert isinstance(dec, float)
        assert isinstance(morph_type, str)
        assert isinstance(redshift, float)
        assert isinstance(size, float)

        self.name = name
        self.ra = ra
        self.dec = dec
        self.morph_type = morph_type
        self.redshift = redshift
        self.size = size

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "name": self.name,
            "ra": self.ra,
            "dec": self.dec,
            "morph_type": self.morph_type,
            "redshift": self.redshift,
            "size": self.size
        }

    def __repr__(self):
        return "<Galaxy %r>" % self.name


def load_db():

    #Creates tables based on models.py
    db.create_all()

    planets_json = json.loads(open('../data/planets.json').read())
    galaxies_json = json.loads(open('../data/galaxies.json').read())
    satellites_json = json.loads(open('../data/satellites.json').read())
    stars_json = json.loads(open('../data/stars.json').read())
    
    galaxies = create_galaxy_objs(galaxies_json)
    insert_into_db(galaxies)
    
    stars = create_star_objs(stars_json)
    insert_into_db(stars)
    
    planets = create_planet_objs(planets_json)
    insert_into_db(planets)
    
    satellites = create_satellite_objs(satellites_json)
    insert_into_db(satellites)

def insert_into_db(*models):
    for table in models:
      for row in table:
        pass
        db.session.add(row)
      db.session.commit()

def create_galaxy_objs(galaxies_json):
    galaxies = []
    for galaxy in galaxies_json:
      galaxy_pid = galaxy.pop("pid")
      galaxies.append(Galaxy(**galaxy))
    
    return galaxies

def create_star_objs(stars_json):
    stars = []
    for star in stars_json:
      star_pid = star.pop("pid")
      galaxy_pid = star.pop("galaxy_pid")

      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Star must reside in a galaxy
      
      star_ref = Star(galaxy=host_galaxy, **star)
      stars.append(star_ref)
      
    return stars

def create_planet_objs(planets_json):
    planets = []
    
    for planet in planets_json:
      planet_pid = planet.pop("pid")
      star_pid = planet.pop("star_pid")
      galaxy_pid = planet.pop("galaxy_pid")
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Planet must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Planet must be in a galaxy 
      
      planet_ref = Planet(star=host_star, galaxy=host_galaxy, **planet)
      planets.append(planet_ref)

    return planets

def create_satellite_objs(satellites_json):
    satellites = []
    
    for sat in satellites_json:
      sat.pop("pid")

      planet_pid = sat.pop("planet_pid")
      star_pid = sat.pop("star_pid")
      galaxy_pid = sat.pop("galaxy_pid")
      
      host_planet = Planet.query.get(planet_pid)
      assert host_planet != None # Satellite must orbit a planet
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Satellite must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Satellite must be in a galaxy 
      
      satellite_ref = Satellite(planet=host_planet, star=host_star, galaxy=host_galaxy, **sat)
      satellites.append(satellite_ref)
      
    return satellites

load_db()
