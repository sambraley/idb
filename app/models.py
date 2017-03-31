#!/usr/bin/env python3
# pylint: disable = invalid-name
# pylint: disable = import-error
# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments
"""
This module is designed to model galaxies, stars, planetoid bodies, and satellites for
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
    and year launched. They may relate many-to-one to galaxies, stars, and planetoid bodies.
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
    # Satellite has a pointer to its star, planetoid body, and galaxy (should they exist)
    # via backreferences.

    # We have at most one of each of these
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    planet_pid = db.Column(
        db.Integer, db.ForeignKey('planet.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # Methods
    def __init__(self, image, year_launched, name, type_of_mission, info_url, agency):
        """
        name a str, agency a str, type_of_mission a str, year_launched an int.
        """
        # Check types
        assert isinstance(image, str)
        assert isinstance(year_launched, str)  # type coming in from json
        assert isinstance(name, str)
        assert isinstance(type_of_mission, str)
        assert isinstance(info_url, str)
        assert isinstance(agency, str)

        self.image = image
        self.year_launched = int(
            year_launched)  # will raise exception if malformed
        self.name = name
        self.type_of_mission = type_of_mission
        self.agency = agency

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
    to satellites and planetoid bodies.
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
    planetoid_bodies = db.relationship(
        'PlanetoidBody', backref='star', lazy='dynamic')
    satellites = db.relationship(
        'Satellite', backref='star', lazy='dynamic')

    # Methods
    def __init__(
            self, temperature, diameter, name, mass, declination, right_ascension,
            planetoid_bodies=(), satellites=()):
        """
        name a str, image a str, temperature, right_ascension, declination, and mass
        are all floats. planetoid_bodies and satellites are to be iterables containing
        instances of the respective classes which orbit this star.
        """
        # Check types
        assert isinstance(temperature, float)
        assert isinstance(diameter, float)
        assert isinstance(name, str)
        assert isinstance(mass, float)
        assert isinstance(declination, float)
        assert isinstance(right_ascension, float)

        self.temperature = temperature
        self.diameter = diameter
        self.name = name
        self.mass = mass
        self.declination = declination
        self.right_ascension = right_ascension
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

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
    to satellites, stars, and planetoid bodies.
    """

    # Attributes
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    image = db.Column(db.String())
    right_ascension = db.Column(db.Float)
    declination = db.Column(db.Float)
    galaxy_type = db.Column(db.String())
    redshift = db.Column(db.Float)
    angular_size = db.Column(db.Float)

    # Relations

    # We could have many of all of these
    stars = db.relationship('Star', backref='galaxy', lazy='dynamic')
    planetoid_bodies = db.relationship(
        'PlanetoidBody', backref='galaxy', lazy='dynamic')
    satellites = db.relationship(
        'Satellite', backref='galaxy', lazy='dynamic')

    # Methods
    # stars, planetoid_bodies, and satellites are to be iterables containing instances
    # of the respective classes which are within this galaxy
    def __init__(
            self, name, image, right_ascension, declination, galaxy_type, redshift,
            angular_size, stars=(), planetoid_bodies=(), satellites=()):
        """
        name a str, image a str, right_ascension and declination floats, galaxy_type a str,
        redshift and angular_size floats. stars, planetoid_bodies, and satellites are to
        be iterables containing instances of the respective classes which are in this galaxy.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(image, str)
        assert isinstance(right_ascension, float)
        assert isinstance(declination, float)
        assert isinstance(galaxy_type, str)
        assert isinstance(redshift, float)
        assert isinstance(angular_size, float)

        self.name = name
        self.image = image
        self.right_ascension = right_ascension
        self.declination = declination
        self.galaxy_type = galaxy_type
        self.redshift = redshift
        self.angular_size = angular_size
        self.stars = stars
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {"name": self.name,
                "image": self.image, "right_ascension": self.right_ascension,
                "declination": self.declination, "galaxy_type": self.galaxy_type,
                "redshift": self.redshift, "angular_size": self.angular_size, "stars": self.stars,
                "planetoid_bodies": self.planetoid_bodies, "satellites": self.satellites}

# Planets, moons, comets, asteroids ...


class PlanetoidBody(db.Model):

    """
    Models planetoids. Attributes are: name, image, diameter, right_ascension,
    declination, gravity, orbital period, mass, and temperature. They may relate
    many-to-one to galaxies and stars, and one-to-many to satellites and other planetoid bodies.
    """

    # Attributes
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    image = db.Column(db.String())
    diameter = db.Column(db.Float)
    right_ascension = db.Column(db.Float)
    declination = db.Column(db.Float)
    gravity = db.Column(db.Float)
    orbital_period = db.Column(db.Float)
    mass = db.Column(db.Float)
    surface_temperature = db.Column(db.Float)

    # Relations
    # Planetoid Bodies have pointers to their galaxies, stars, and host (planetoid body they orbit)
    # via backreference

    # We have at most one of these
    host_id = db.Column(db.Integer, db.ForeignKey('planetoid_body.pid'))
    star_id = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))

    # We could have many of these
    orbiting_bodies = db.relationship(
        'PlanetoidBody', backref='host', remote_side=pid)
    satellites = db.relationship(
        'Satellite', backref='host', lazy='dynamic')

    # Methods
    # orbiting_bodies, and satellites are to be iterables containing instances of the respective
    # classes which are within this galaxy
    def __init__(
            self, name, image, diameter, surface_temperature, right_ascension, declination,
            mass, gravity, orbital_period, orbiting_bodies=None, satellites=()):
        """
        name a str, image a str, diameter, surface_temperature, right_ascension, declination,
        mass, gravity, orbital_period are all floats. orbiting_bodies and satellites are to be
        iterables containing instances of the respective classes which orbit this planetoid.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(image, str)
        assert isinstance(diameter, float)
        assert isinstance(surface_temperature, float)
        assert isinstance(right_ascension, float)
        assert isinstance(declination, float)
        assert isinstance(mass, float)
        assert isinstance(gravity, float)
        assert isinstance(orbital_period, float)

        self.name = name
        self.image = image
        self.diameter = diameter
        self.surface_temperature = surface_temperature
        self.right_ascension = right_ascension
        self.declination = declination
        self.mass = mass
        self.gravity = gravity
        self.orbital_period = orbital_period
        self.orbiting_bodies = orbiting_bodies
        self.satellites = satellites

    def dictionary(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "name": self.name, "image": self.image, "diameter": self.diameter,
            "temperature": self.surface_temperature, "right_ascension": self.right_ascension,
            "declination": self.declination, "mass": self.mass, "gravity": self.gravity,
            "orbital_period": self.orbital_period, "orbiting_bodies": self.orbiting_bodies,
            "satellites": self.satellites}
