#!/usr/bin/env python3
# pylint: disable = invalid-name
# pylint: disable = import-error
# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from idb import app

db = SQLAlchemy(app)


class Satellite(db.Model):

    """Models artificial satellites, tracking their name, agency, mission type,
    and year launched"""

    # Attributes
    identifier = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    agency = db.Column(db.String())
    mission = db.Column(db.String())
    year_launched = db.Column(db.Integer)

    # Relations
    # Satellite has a pointer to its star, planetoid body, and galaxy (should they exist)
    # via backreferences.

    # We have at most one of each of these
    star_id = db.Column(db.Integer, db.ForeignKey('star.identifier'))
    planetoid_id = db.Column(
        db.Integer, db.ForeignKey('planetoid_body.identifier'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.identifier'))

    # Methods
    def __init__(self, name, agency, type_of_mission, year_launched):
        # Check types
        assert isinstance(name, str)
        assert isinstance(agency, str)
        assert isinstance(type_of_mission, str)
        assert isinstance(year_launched, int)

        self.name = name
        self.agency = agency
        self.type_of_mission = type_of_mission
        self.year_launched = year_launched

    def dictionary(self):
        return {
            "name": self.name, "agency": self.agency, "mission": self.mission,
            "year launched": self.year_launched}


class Star(db.Model):

    """Models stars"""

    # Attributes
    identifier = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    image = db.Column(db.String())
    temperature = db.Column(db.Float)
    right_ascension = db.Column(db.Float)
    declination = db.Column(db.Float)
    mass = db.Column(db.Float)

    # Relations
    # Stars have a pointer to their galaxy via backreference

    # We have at most one of these
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.identifier'))

    # We could have many of these
    planetoid_bodies = db.relationship(
        'PlanetoidBody', backref='star', lazy='dynamic')
    satellites = db.relationship(
        'Satellite', backref='star', lazy='dynamic')

    # Methods
    # planetoid_bodies and satellites are to be iterables containing instances of the respective
    # classes which orbit this star
    def __init__(
            self, name, image, temperature, right_ascension, declination, mass,
            planetoid_bodies=None, satellites=None):
        # Check types
        assert isinstance(name, str)
        assert isinstance(image, str)
        assert isinstance(temperature, float)
        assert isinstance(right_ascension, float)
        assert isinstance(declination, float)
        assert isinstance(mass, float)

        self.name = name
        self.image = image
        self.temperature = temperature
        self.right_ascension = right_ascension
        self.declination = declination
        self.mass = mass
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

    def dictionary(self):
        return {
            "name": self.name, "image": self.image, "temperature": self.temperature,
            "right ascension": self.right_ascension, "declination": self.declination,
            "mass": self.mass, "planetoid bodies": self.planetoid_bodies,
            "satellites": self.satellites}


class Galaxy(db.Model):
    # Attributes
    identifier = db.Column(db.Integer, primary_key=True)
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
            angular_size, stars=None, planetoid_bodies=None, satellites=None):
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
        return {"name": self.name,
                "image": self.image, "right ascension": self.right_ascension,
                "declination": self.declination, "galaxy type": self.galaxy_type,
                "redshift": self.redshift, "angular size": self.angular_size, "stars": self.stars,
                "planetoid bodies": self.planetoid_bodies, "satellites": self.satellites}

# Planets, moons, comets, asteroids ...


class PlanetoidBody(db.Model):
    # Attributes
    identifier = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
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
    host_id = db.Column(db.Integer, db.ForeignKey('planetoid_body.identifier'))
    star_id = db.Column(db.Integer, db.ForeignKey('star.identifier'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.identifier'))

    # We could have many of these
    orbiting_bodies = db.relationship(
        'PlanetoidBody', backref='host', remote_side=identifier)
    satellites = db.relationship(
        'Satellite', backref='planetoid_body', lazy='dynamic')

    # Methods
    # orbiting_bodies, and satellites are to be iterables containing instances of the respective
    # classes which are within this galaxy
    def __init__(
            self, name, image, diameter, surface_temperature, right_ascension, declination,
            mass, gravity, orbital_period, orbiting_bodies=None, satellites=None):
        # Check types
        assert isinstance(name, str)
        assert isinstance(image, str)
        assert isinstance(diameter, float)
        assert isinstance(surface_temperature, float)
        assert isinstance(right_ascension, float)
        assert isinstance(declination, float)
        assert isinstance(mass, float)
        assert isinstance(gravity, str)
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
        return {
            "name": self.name, "image": self.image, "diameter": self.diameter,
            "temperature": self.surface_temperature, "right ascension": self.right_ascension,
            "declination": self.declination, "mass": self.mass, "gravity": self.gravity,
            "orbital period": self.orbital_period, "orbiting bodies": self.orbiting_bodies,
            "satellites": self.satellites}