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

from flask_sqlalchemy import SQLAlchemy
from idb import app

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/dummy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Satellite(db.Model):

    """
    Models artificial satellites. Attributes are: name, agency, mission type,
    and year launched. They may relate many-to-one to galaxies, stars, and planets.
    """

    # Attributes
    image = db.Column(db.String())
    year_launched = db.Column(db.Integer)
    name = db.Column(db.String(), unique=True)
    mission = db.Column(db.String())
    info_url = db.Column(db.String())
    pid = db.Column(db.Integer, primary_key=True)
    agency = db.Column(db.String())

    # Relations
    # Satellite has a pointer to its star, planet, and galaxy (should they exist)
    # via backreferences.

    # We have at most one of each of these
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    planet_pid = db.Column(
        db.Integer, db.ForeignKey('planet.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # Methods
#    def __init__(self, image, year_launched, name, type_of_mission, info_url, agency, **kwargs):
#        """
#        name a str, agency a str, type_of_mission a str, year_launched an int.
#        """
#        # Check types
#        assert isinstance(image, str)
#        assert isinstance(year_launched, str)  # type coming in from json
#        assert isinstance(name, str)
#        assert isinstance(type_of_mission, str)
#        assert isinstance(info_url, str)
#        assert isinstance(agency, str)
#
#        self.image = image
#        self.year_launched = int(
#            year_launched)  # will raise exception if malformed
#        self.name = name
#        self.type_of_mission = type_of_mission
#        self.agency = agency
#
#        super(Satellite, self).__init__(**kwargs)

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "image": self.image,
            "year_launched": self.year_launched,
            "name": self.name,
            "star_pid": self.star_pid,
            "type": self.mission,
            "info_url": self.info_url,
            "pid": self.pid,
            "planet_pid": self.planet_pid,
            "agency": self.agency,
            "galaxy_pid": self.galaxy_pid
        }


class Star(db.Model):

    """
    Models stars. Attributes are: name, image, temperature, right_ascension,
    declination, and mass. They may relate many-to-one to galaxies and one-to-many
    to satellites and planets.
    """

    # Attributes
    temperature = db.Column(db.Float)
    diameter = db.Column(db.Float)
    name = db.Column(db.String(), unique=True)
    mass = db.Column(db.Float)
    pid = db.Column(db.Integer, primary_key=True)
    declination = db.Column(db.Float)
    right_ascension = db.Column(db.Float)

    # Relations
    # Stars have a pointer to their galaxy via backreference

    # We have at most one of these
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # We could have many of these
    planets = db.relationship(
        'Planet', backref='star', lazy='dynamic')
    satellites = db.relationship(
        'Satellite', backref='star', lazy='dynamic')

    # Methods
#    def __init__(
#            self, temperature, diameter, name, mass, declination, right_ascension,
#            planets=(), satellites=()):
#        """
#        name a str, image a str, temperature, right_ascension, declination, and mass
#        are all floats. planets and satellites are to be iterables containing
#        instances of the respective classes which orbit this star.
#        """
#        # Check types
#        assert isinstance(temperature, float)
#        assert isinstance(diameter, float)
#        assert isinstance(name, str)
#        assert isinstance(mass, float)
#        assert isinstance(declination, float)
#        assert isinstance(right_ascension, float)
#
#        self.temperature = temperature
#        self.diameter = diameter
#        self.name = name
#        self.mass = mass
#        self.declination = declination
#        self.right_ascension = right_ascension
#        self.planets = planets
#        self.satellites = satellites

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "temperature": self.temperature,
            "diameter": self.diameter,
            "name": self.name,
            "mass": self.mass,
            "pid": self.pid,
            "dec": self.declination,
            "ra": self.right_ascension,
            "galaxy_pid": self.galaxy_pid
        }


class Galaxy(db.Model):

    """
    Models galaxies. Attributes are: name, image, right_ascension, declination,
    galaxy type (spiral, etc), redshift, and angular size. They may relate one-to-many
    to satellites, stars, and planets.
    """

    # Attributes
    redshift = db.Column(db.Float)
    name = db.Column(db.String(), unique=True)
    galaxy_type = db.Column(db.String())
    size = db.Column(db.Float)
    pid = db.Column(db.Integer, primary_key=True)
    declination = db.Column(db.Float)
    right_ascension = db.Column(db.Float)

    # Relations

    # We could have many of all of these
    stars = db.relationship('Star', backref='galaxy', lazy='dynamic')
    planets = db.relationship(
        'Planet', backref='galaxy', lazy='dynamic')
    satellites = db.relationship(
        'Satellite', backref='galaxy', lazy='dynamic')

    # Methods
    # stars, planets, and satellites are to be iterables containing instances
    # of the respective classes which are within this galaxy
#    def __init__(
#            self, redshift, name, galaxy_type, size, declination, right_ascension,
#            stars=(), planets=(), satellites=()):
#        """
#        name a str, image a str, right_ascension and declination floats, galaxy_type a str,
#        redshift and angular_size floats. stars, planets, and satellites are to
#        be iterables containing instances of the respective classes which are in this galaxy.
#        """
#        # Check types
#        assert isinstance(redshift, float)
#        assert isinstance(name, str)
#        assert isinstance(galaxy_type, str)
#        assert isinstance(size, float)
#        assert isinstance(declination, float)
#        assert isinstance(right_ascension, float)
#
#        self.redshift = redshift
#        self.name = name
#        self.galaxy_type = galaxy_type
#        self.size = size
#        self.declination = declination
#        self.right_ascension = right_ascension
#        self.stars = stars
#        self.planets = planets
#        self.satellites = satellites

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "redshift": self.redshift,
            "name": self.name,
            "type": self.galaxy_type,
            "size": self.size,
            "dec": self.declination,
            "ra": self.right_ascension
        }


class Planet(db.Model):

    """
    Models planets. Attributes are: name, image, diameter, right_ascension,
    declination, gravity, orbital period, mass, and temperature. They may relate
    many-to-one to galaxies and stars, and one-to-many to satellites and other planets.
    """

    # Attributes
    temperature = db.Column(db.Float)
    diameter = db.Column(db.Float)
    name = db.Column(db.String(), unique=True)
    orbital_period = db.Column(db.Float)
    mass = db.Column(db.Float)
    pid = db.Column(db.Integer, primary_key=True)
    declination = db.Column(db.Float)
    right_ascension = db.Column(db.Float)
    gravity = db.Column(db.Float)

    # Relations
    # Planets have pointers to their galaxies, stars, and host (planet body they orbit)
    # via backreference

    # We have at most one of these
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # We could have many of these
    satellites = db.relationship(
        'Satellite', backref='host', lazy='dynamic')

    # Methods
    # orbiting_bodies, and satellites are to be iterables containing instances of the respective
    # classes which are within this galaxy
#    def __init__(
#            self, temperature, diameter, name, orbital_period, mass, declination,
#            right_ascension, gravity, satellites=()):
#        """
#        name a str, image a str, diameter, surface_temperature, right_ascension, declination,
#        mass, gravity, orbital_period are all floats. orbiting_bodies and satellites are to be
#        iterables containing instances of the respective classes which orbit this planet.
#        """
#        # Check types
#        assert isinstance(temperature, float)
#        assert isinstance(diameter, float)
#        assert isinstance(name, str)
#        assert isinstance(orbital_period, float)
#        assert isinstance(mass, float)
#        assert isinstance(declination, float)
#        assert isinstance(right_ascension, float)
#        assert isinstance(gravity, float)
#
#        self.temperature = temperature
#        self.diameter = diameter
#        self.name = name
#        self.orbital_period = orbital_period
#        self.mass = mass
#        self.declination = declination
#        self.right_ascension = right_ascension
#        self.gravity = gravity
#        self.satellites = satellites

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "temperature": self.temperature,
            "diameter": self.diameter,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "mass": self.mass,
            "star_pid": self.star_pid,
            "pid": self.pid,
            "dec": self.declination,
            "ra": self.right_ascension,
            "galaxy_pid": self.galaxy_pid,
            "gravity": self.gravity
        }
