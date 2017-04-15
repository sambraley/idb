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

@whooshee.register_model('name', 'year_launched', 'mission_type', 'agency')
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
<<<<<<< HEAD
=======
    img_url = db.Column(db.Text())
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
    year_launched = db.Column(db.String())
    mission_type = db.Column(db.String())
    info_url = db.Column(db.String())
    agency = db.Column(db.String())

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
        self.year_launched = str(year_launched)
        self.mission_type = mission_type
        self.info_url = info_url
        self.agency = agency
        self.planet = planet
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
            "year_launched": int(self.year_launched),
            "mission_type": self.mission_type,
            "info_url": self.info_url,
            "agency": self.agency,
            "planet_pid": self.planet_pid,
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Satellite %r>" % self.name

@whooshee.register_model('name', 'diameter', 'ra', 'dec', 'gravity', 'orbital_period', 'mass', 'temperature')
class Planet(db.Model):

    """
<<<<<<< HEAD
    Models planets. Attributes are: name, diameter, right_ascension,
=======
    Models planets. Attributes are: name, img_url, diameter, right_ascension,
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
    diameter = db.Column(db.String())
    ra = db.Column(db.String())
    dec = db.Column(db.String())
    gravity = db.Column(db.String())
    orbital_period = db.Column(db.String())
    mass = db.Column(db.String())
    temperature = db.Column(db.String())
<<<<<<< HEAD
=======
    img_url = db.Column(db.Text())
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e

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
        self.diameter = str(diameter)
        self.ra = str(ra)
        self.dec = str(dec)
        self.gravity = str(gravity)
        self.orbital_period = str(orbital_period)
        self.mass = str(mass)
        self.temperature = str(temperature)
<<<<<<< HEAD
=======
        self.img_url = img_url
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
            "diameter": float(self.diameter),
            "ra": float(self.ra),
            "dec": float(self.dec),
            "gravity": float(self.gravity),
            "orbital_period": float(self.orbital_period),
            "mass": float(self.mass),
            "temperature": int(self.temperature),
            "star_pid": self.star_pid,
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Planet %r>" % self.name


@whooshee.register_model('name', 'diameter', 'ra', 'dec', 'temperature', 'mass')
class Star(db.Model):

    """
<<<<<<< HEAD
    Models stars. Attributes are: name, temperature, right_ascension,
=======
    Models stars. Attributes are: name, img_url, temperature, right_ascension,
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
    diameter = db.Column(db.String())
    ra = db.Column(db.String())
    dec = db.Column(db.String())
    temperature = db.Column(db.String())
    mass = db.Column(db.String())
<<<<<<< HEAD
=======
    img_url = db.Column(db.Text())
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e

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
        self.ra = str(ra)
        self.dec = str(dec)
        self.temperature = str(temperature)
        self.mass = str(mass)
<<<<<<< HEAD
=======
        self.img_url = img_url
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
            "ra": float(self.ra),
            "dec": float(self.dec),
            "temperature": int(self.temperature),
            "mass": float(self.mass),
            "galaxy_pid": self.galaxy_pid
        }

    def __repr__(self):
        return "<Star %r>" % self.name


@whooshee.register_model('name', 'ra', 'dec', 'morph_type', 'size', 'redshift')
class Galaxy(db.Model):

    """
<<<<<<< HEAD
    Models galaxies. Attributes are: name, right_ascension, declination,
=======
    Models galaxies. Attributes are: name, img_url, right_ascension, declination,
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
    ra = db.Column(db.String())
    dec = db.Column(db.String())
    morph_type = db.Column(db.String())
    redshift = db.Column(db.String())
    size = db.Column(db.String())
<<<<<<< HEAD
    
    # Foreign Keys
    image_pid = db.Column(db.Integer, db.ForeignKey("image.pid"))
    
    # Relations
    image = db.relationship(
        "Image", backref="Galaxy")
        
=======
    img_url = db.Column(db.String())

>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e
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
        self.ra = str(ra)
        self.dec = str(dec)
        self.morph_type = morph_type
        self.redshift = str(redshift)
        self.size = str(size)
<<<<<<< HEAD
        self.image = image
=======
        self.img_url = img_url
>>>>>>> c39878b10c2e24cbfaa721dac84713821e3ba16e

    def to_dict(self):
        """
        Returns a dictionary representation of this model.
        """
        return {
            "name": self.name,
            "ra": float(self.ra),
            "dec": float(self.dec),
            "morph_type": self.morph_type,
            "redshift": float(self.redshift),
            "size": float(self.size),
        }

    def __repr__(self):
        return "<Galaxy %r>" % self.name
