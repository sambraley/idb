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

test_db = SQLAlchemy()

class Satellite(test_db.Model):

    """
    Models artificial satellites. Attributes are: name, agency, mission type,
    and year launched. They may relate many-to-one to galaxies, stars, and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = test_db.Column(test_db.Integer, primary_key=True)

    # Model Attributes
    name = test_db.Column(test_db.String(), unique=True)
    img_url = test_db.Column(test_db.String())
    year_launched = test_db.Column(test_db.Integer)
    mission_type = test_db.Column(test_db.String())
    info_url = test_db.Column(test_db.String())
    agency = test_db.Column(test_db.String())

    # Foreign Keys
    planet_pid = test_db.Column(test_db.Integer, test_db.ForeignKey('planet.pid'))
    star_pid = test_db.Column(test_db.Integer, test_db.ForeignKey('star.pid'))
    galaxy_pid = test_db.Column(test_db.Integer, test_db.ForeignKey('galaxy.pid'))

    # Relations
    planet = test_db.relationship(
        "Planet", backref=test_db.backref("satellites", lazy="dynamic"))
    star = test_db.relationship(
        "Star", backref=test_db.backref("satellites", lazy="dynamic"))
    galaxy = test_db.relationship(
        "Galaxy", backref=test_db.backref("satellites", lazy="dynamic"))

    #
    # Methods
    #

    def __init__(
            self, name, img_url, year_launched, mission_type, info_url, agency,
            planet, star, galaxy):
        """
        name a str, agency a str, mission_type a str, year_launched an int.
        """
        # Check types
        assert isinstance(img_url, str)
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
        self.img_url = img_url
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
            "img_url": self.img_url,
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

class Planet(test_db.Model):

    """
    Models planets. Attributes are: name, img_url, diameter, right_ascension,
    declination, gravity, orbital period, mass, and temperature. They may relate
    many-to-one to galaxies and stars, and one-to-many to satellites and other planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = test_db.Column(test_db.Integer, primary_key=True)

    # Model Attributes
    name = test_db.Column(test_db.String(), unique=True)
    img_url = test_db.Column(test_db.String())
    diameter = test_db.Column(test_db.Float)
    ra = test_db.Column(test_db.Float)
    dec = test_db.Column(test_db.Float)
    gravity = test_db.Column(test_db.Float)
    orbital_period = test_db.Column(test_db.Float)
    mass = test_db.Column(test_db.Float)
    temperature = test_db.Column(test_db.Integer)

    # Foreign Keys
    star_pid = test_db.Column(test_db.Integer, test_db.ForeignKey('star.pid'))
    galaxy_pid = test_db.Column(test_db.Integer, test_db.ForeignKey('galaxy.pid'))

    # Relations
    star = test_db.relationship(
        "Star", backref=test_db.backref("planets", lazy="dynamic"))
    galaxy = test_db.relationship(
        "Galaxy", backref=test_db.backref("planets", lazy="dynamic"))

    #
    # Methods
    #

    def __init__(
            self, name, img_url, diameter, ra, dec, gravity, orbital_period, mass,
            temperature, star, galaxy):
        """
        name a str, img_url a str, diameter, temperature, right_ascension, declination,
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
        self.img_url = img_url
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
            "img_url": self.img_url,
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


class Star(test_db.Model):

    """
    Models stars. Attributes are: name, img_url, temperature, right_ascension,
    declination, and mass. They may relate many-to-one to galaxies and one-to-many
    to satellites and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = test_db.Column(test_db.Integer, primary_key=True)

    # Model Attributes
    name = test_db.Column(test_db.String(), unique=True)
    img_url = test_db.Column(test_db.String())
    diameter = test_db.Column(test_db.Float)
    ra = test_db.Column(test_db.Float)
    dec = test_db.Column(test_db.Float)
    temperature = test_db.Column(test_db.Integer)
    mass = test_db.Column(test_db.Float)

    # Foreign Keys
    galaxy_pid = test_db.Column(test_db.Integer, test_db.ForeignKey("galaxy.pid"))

    # Relations
    galaxy = test_db.relationship(
        "Galaxy", backref=test_db.backref("stars", lazy='dynamic'))

    #
    # Methods
    #

    def __init__(self, name, img_url, diameter, ra, dec, temperature, mass, galaxy):
        """
        name a str, img_url a str, temperature, right_ascension, declination, and mass
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
        self.img_url = img_url
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
            "img_url": self.img_url,
            "diameter": self.diameter,
            "ra": self.ra,
            "dec": self.dec,
            "temperature": self.temperature,
            "mass": self.mass,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Star %r>" % self.name


class Galaxy(test_db.Model):

    """
    Models galaxies. Attributes are: name, img_url, right_ascension, declination,
    galaxy type (spiral, etc), redshift, and angular size. They may relate one-to-many
    to satellites, stars, and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = test_db.Column(test_db.Integer, primary_key=True)

    # Model Attributes
    name = test_db.Column(test_db.String(), unique=True)
    img_url = test_db.Column(test_db.String())
    ra = test_db.Column(test_db.Float)
    dec = test_db.Column(test_db.Float)
    morph_type = test_db.Column(test_db.String())
    redshift = test_db.Column(test_db.Float)
    size = test_db.Column(test_db.Float)

    #
    # Methods
    #

    def __init__(self, name, img_url, ra, dec, morph_type, redshift, size):
        """
        name a str, img_url a str, right_ascension and declination floats, galaxy_type a str,
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
        self.img_url = img_url
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
            "img_url": self.img_url,
            "ra": self.ra,
            "dec": self.dec,
            "morph_type": self.morph_type,
            "redshift": self.redshift,
            "size": self.size
        }

    def __repr__(self):
        return "<Galaxy %r>" % self.name
