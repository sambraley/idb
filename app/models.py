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
from database import db, whooshee

class Image(db.Model):
    """
    Models image urls for all objects. Attributes are img_url.
    Image relates one-to-one to all other models
    """

    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    img_url = db.Column(db.Text)

     #
    # Methods
    #

    def __init__(self, img_url):
        assert isinstance(img_url, str)
        self.img_url = img_url

@whooshee.register_model('name', 'year_launched_str', 'mission_type', 'agency')
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
    year_launched = db.Column(db.Integer)
    mission_type = db.Column(db.String())
    info_url = db.Column(db.String())
    agency = db.Column(db.String())

    # String attributes for searching
    year_launched_str = db.Column(db.String())

    # Foreign Keys
    planet_pid = db.Column(db.Integer, db.ForeignKey('planet.pid'))
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))
    image_pid = db.Column(db.Integer, db.ForeignKey('image.pid'))

    # Relations
    planet = db.relationship(
        "Planet", backref=db.backref("satellites", lazy="dynamic"))
    star = db.relationship(
        "Star", backref=db.backref("satellites", lazy="dynamic"))
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("satellites", lazy="dynamic"))
    image = db.relationship(
        "Image", backref="Satellite")
    #
    # Methods
    #

    def __init__(
            self, name, year_launched, mission_type, info_url, agency,
            planet, star, galaxy, image):
        """
        name a str, info_url a str, agency a str, mission_type a str, year_launched an int.
        """
        # Check types
        assert isinstance(year_launched, int)
        assert isinstance(name, str)
        assert isinstance(mission_type, str)
        assert isinstance(info_url, str)
        assert isinstance(agency, str)
        assert isinstance(planet, Planet)
        assert isinstance(star, Star)
        assert isinstance(galaxy, Galaxy)
        assert isinstance(image, Image)

        # Create instance
        self.name = name
        self.year_launched = year_launched
        self.mission_type = mission_type
        self.info_url = info_url
        self.agency = agency
        self.planet = planet
        self.star = star
        self.galaxy = galaxy
        self.image = image

        # String attributes for searching
        self.year_launched_str = str(year_launched)

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "year_launched": self.year_launched,
            "mission_type": self.mission_type,
            "info_url": self.info_url,
            "agency": self.agency,
            "planet_pid": self.planet_pid,
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid,
            "model_type": self.__class__.__name__
        }
    
    def model_type(self):
        return self.__class__.__name__

    def __repr__(self):
        return "<Satellite %r>" % self.name

@whooshee.register_model('name', 'diameter_str', 'ra_str', 'dec_str', 'gravity_str',
                         'orbital_period_str', 'mass_str', 'temperature_str')
class Planet(db.Model):

    """
    Models planets. Attributes are: name, diameter, right_ascension,
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

    # String attributes for searching
    diameter_str = db.Column(db.String())
    ra_str = db.Column(db.String())
    dec_str = db.Column(db.String())
    gravity_str = db.Column(db.String())
    orbital_period_str = db.Column(db.String())
    mass_str = db.Column(db.String())
    temperature_str = db.Column(db.String())

    # Foreign Keys
    star_pid = db.Column(db.Integer, db.ForeignKey('star.pid'))
    galaxy_pid = db.Column(db.Integer, db.ForeignKey('galaxy.pid'))
    image_pid = db.Column(db.Integer, db.ForeignKey('image.pid'))

    # Relations
    star = db.relationship(
        "Star", backref=db.backref("planets", lazy="dynamic"))
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("planets", lazy="dynamic"))
    image = db.relationship(
        "Image", backref="Planet")

    #
    # Methods
    #

    def __init__(
            self, name, diameter, ra, dec, gravity, orbital_period, mass,
            temperature, star, galaxy, image):
        """
        name a str, diameter a float, temperature a int, right_ascension, declination,
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
        assert isinstance(image, Image)

        # Create Instance
        self.name = name
        self.diameter = diameter
        self.ra = ra
        self.dec = dec
        self.gravity = gravity
        self.orbital_period = orbital_period
        self.mass = mass
        self.temperature = temperature

        self.diameter_str = str(diameter)
        self.ra_str = str(ra)
        self.dec_str = str(dec)
        self.gravity_str = str(gravity)
        self.orbital_period_str = str(orbital_period)
        self.mass_str = str(mass)
        self.temperature_str = str(temperature)

        self.star = star
        self.galaxy = galaxy
        self.image = image

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
            "galaxy_pid": self.galaxy_pid,
            "model_type": self.__class__.__name__
        }

    def model_type(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return "<Planet %r>" % self.name


@whooshee.register_model('name', 'diameter_str', 'ra_str', 'dec_str', 'temperature_str', 'mass_str')
class Star(db.Model):

    """
    Models stars. Attributes are: name, temperature, right_ascension,
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
    
    # String attributes for searching
    diameter_str = db.Column(db.String())
    ra_str = db.Column(db.String())
    dec_str = db.Column(db.String())
    temperature_str = db.Column(db.String())
    mass_str = db.Column(db.String())

    # Foreign Keys
    galaxy_pid = db.Column(db.Integer, db.ForeignKey("galaxy.pid"))
    image_pid = db.Column(db.Integer, db.ForeignKey("image.pid"))

    # Relations
    galaxy = db.relationship(
        "Galaxy", backref=db.backref("stars", lazy='dynamic'))

    image = db.relationship(
        "Image", backref="Star")

    #
    # Methods
    #

    def __init__(self, name, diameter, ra, dec, temperature, mass, galaxy, image):
        """
        name a str, temperature a int, right_ascension, declination, and mass
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
        assert isinstance(image, Image)

        # Create instance
        self.name = name
        self.diameter = diameter
        self.ra = ra
        self.dec = dec
        self.temperature = temperature
        self.mass = mass
        self.galaxy = galaxy
        self.image = image
      
        self.diameter_str = str(diameter)
        self.ra_str = str(ra)
        self.dec_str = str(dec)
        self.temperature_str = str(temperature)
        self.mass_str = str(mass)

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
            "galaxy_pid": self.galaxy_pid,
            "model_type": self.__class__.__name__
        }

    def model_type(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return "<Star %r>" % self.name


@whooshee.register_model('name', 'ra_str', 'dec_str', 'morph_type', 'size_str', 'redshift_str')
class Galaxy(db.Model):

    """
    Models galaxies. Attributes are: name, right_ascension, declination,
    galaxy type (spiral, etc), redshift, and angular size. They may relate one-to-many
    to satellites, stars, and planets.
    """
    #
    # Attributes
    #

    # Primary Key
    pid = db.Column(db.Integer, primary_key=True)

    # Model Attributes
    name = db.Column(db.String, unique=True)
    ra = db.Column(db.Float)
    dec = db.Column(db.Float)
    morph_type = db.Column(db.String())
    redshift = db.Column(db.Float)
    size = db.Column(db.Float)

    # String attributes for searching
    ra_str = db.Column(db.String())
    dec_str = db.Column(db.String())
    redshift_str = db.Column(db.String())
    size_str = db.Column(db.String())
    
    # Foreign Keys
    image_pid = db.Column(db.Integer, db.ForeignKey("image.pid"))

    # Relations
    image = db.relationship(
        "Image", backref="Galaxy")

    #
    # Methods
    #

    def __init__(self, name, ra, dec, morph_type, redshift, size, image):
        """
        name a str, right_ascension and declination floats, galaxy_type a str,
        redshift and size floats.
        """
        # Check types
        assert isinstance(name, str)
        assert isinstance(ra, float)
        assert isinstance(dec, float)
        assert isinstance(morph_type, str)
        assert isinstance(redshift, float)
        assert isinstance(size, float)
        assert isinstance(image, Image)

        self.name = name
        self.ra = ra
        self.dec = dec
        self.morph_type = morph_type
        self.redshift = redshift
        self.size = size
        self.image = image

        self.ra_str = str(ra)
        self.dec_str = str(dec)
        self.redshift_str = str(redshift)
        self.size_str = str(size)

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
            "size": self.size,
            "model_type": self.__class__.__name__
        }

    def model_type(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return "<Galaxy %r>" % self.name
