#!/usr/bin/env python3
# pylint: disable = invalid-name
# pylint: disable = import-error
# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-arguments

"""
This module is designed to model galaxies, stars, planets, satellites,
and images for use in a PostgreSQL database using Flask-SQLAlchemy.
"""
from database import db, whooshee


class Image(db.Model):
    """
    Models image urls for all objects. Attributes are:
    img_url: a url of the image
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
        """
        img_url a str of the url
        """
        assert isinstance(img_url, str)
        self.img_url = img_url

    def to_dict(self):
        """
        Returns a dictionary representation of an image
        """
        return {
            "img_url": self.img_url
        }

    @staticmethod
    def model_type():
        """
        Returns the type of this model.
        The type is defined as the plural form of the class name.
        """
        return "images"

    def __repr__(self):
        """
        Returns a string representation of the Satellite
        """
        return "<Image %r>" % self.pid


@whooshee.register_model('name', 'year_launched_str', 'mission_type', 'agency')
class Satellite(db.Model):
    """
    Models artificial satellites. Attributes are: 
    name: The name of the satellite
    agency: The full name of the agency that owns or leads the satellite project
    mission_type: The purpose of the satellite such as Earth Science, Astrophysics etc.
    info_url: a url to a page that contains more information about the satellite
    year launched: The year the satellite was launched

    Satellites may relate many-to-one to galaxies, stars, and planets.

    A string version of year_launched also exists to allow full text
    searches of a database simpler
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
        name a str of the Satellite's name
        info_url a str a url to more information about the satellite
        agency a str of full name of the agency 
        mission_type a str of the mission type
        year_launched an int the year the satellite was launched
        planet a Planet object that the satellite orbits around
        galaxy a Galaxy object that the satellite exists in
        image an Image object that contains the image of the satellite
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
        Returns a dictionary representation of a Satellite
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
            "model_type": Satellite.model_type()
        }

    @staticmethod
    def model_type():
        """
        Returns the type of this model.
        The type is defined as the plural form of the class name.
        """
        return "satellites"

    def __repr__(self):
        """
        Returns a string representation of the Satellite
        """
        return "<Satellite %r>" % self.name


@whooshee.register_model('name', 'diameter_str', 'ra_str', 'dec_str', 'gravity_str',
                         'orbital_period_str', 'mass_str', 'temperature_str')
class Planet(db.Model):

    """
    Models planets. Attributes are: 
    name: The name of the planet 
    diameter: The diameter of the planet in terms of Jupiter diameters
    ra: The right ascension in the ICRS J2000 coordinate system in decimal archour form
    dec: The declination in the ICRS J2000 coordinate system in decimal degree form
    gravity: The surface gravity of the planet in multiples of the Jupiter gravity
    orbital_period: The orbital period of the planet in earth days
    mass: The mass of the planet in Jupiter masses
    temperature: The surface temperature of the planet in Kelvin 

    They may relate many-to-one to galaxies and stars, 
    and one-to-many to satellites.

    String versions of diameter, ra, dec, gravity, oribital_period, mass, and temperature
    also exist to make full text database searching simpler.
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
        name a str of the Planet name
        diameter a float of the Planet diameter in Jupiter diameters
        temperature a int of the surface temperature of the planet
        ra a float of the right ascension
        dec a float of the declination
        mass a float of the mass of the planet in Jupiter masses
        gravity a float of the surface gravity of the planet
        orbital_period a float of the orbital period in earth days.
        star a Star object in which the Star orbits around
        galaxy a Galaxy object in which the planet resides in
        image an Image object containing the image of the planet
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
        Returns a dictionary representation the Planet.
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
            "model_type": Planet.model_type()
        }

    @staticmethod
    def model_type():
        """
        Returns the type of this model.
        The type is defined as the plural form of the class name.
        """
        return "planets"

    def __repr__(self):
        """
        Returns the string representation of the Planet.
        """
        return "<Planet %r>" % self.name


@whooshee.register_model('name', 'diameter_str', 'ra_str', 'dec_str', 'temperature_str', 'mass_str')
class Star(db.Model):

    """
    Models stars. Main attributes are: 
    name: The name of the Star
    diameter: The diameter of the Star in solar diameters
    ra: The right ascension in the ICRS J2000 coordinate system in decimal hour form
    dec: The declination in the ICRS J2000 coordinate system in decimal degree form 
    temperature: The surface temperature of the Star
    mass: The mass of the star in solar masses

    Stars may relate many-to-one to galaxies and one-to-many
    to satellites and planets.

    String versions of diameter, ra, dec, temperature, and mass also exist
    to make full text searches of the database simpler.
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
        name a str of the Star name
        diameter a float of the Star's diameter in Solar diameters
        ra a float of the right ascension
        dec a float of the declination
        temperature an int of the surface temperature
        mass a float of the Star's mass in Solar masses
        galaxy a Galaxy object that the star exists in
        image an Image object of the image for the star
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
        Returns a dictionary representation of this Star.
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
            "model_type": Star.model_type()
        }

    @staticmethod
    def model_type():
        """
        Returns the type of this model.
        The type is defined as the plural form of the class name.
        """
        return "stars"

    def __repr__(self):
        """
        Returns a string representation of the Star.
        """
        return "<Star %r>" % self.name


@whooshee.register_model('name', 'ra_str', 'dec_str', 'morph_type', 'size_str', 'redshift_str')
class Galaxy(db.Model):

    """
    Models galaxies. Attributes are: 
    name: The name of the galaxy 
    ra: The right ascension in the ICRS J2000 coordinate system in decimal archour form
    dec: The declination in the ICRS J2000 coordinate system in decimal degree form
    morph_type: The morphilogical type of the galaxy such as Spiral, Irregular, etc.
    redshift: The redshift of the galaxy
    size: The angular size in decimal arcminutes form of the major axis of the galaxy

    Galaxies may relate one-to-many to satellites, stars, and planets.

    String versions of ra, dec, redshift, and size also exist to allow
    full text searches to be simpler.
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
        name a str of the galaxy name
        ra a float of the right ascension 
        dec a float of the declination
        morph_type a str of the morphilogical type
        redshift a float of the redshift value
        size a float of the angular size
        image a Image object that is the image for the galaxy
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
        Returns a dictionary representation of the Galaxy.
        """
        return {
            "pid": self.pid,
            "name": self.name,
            "ra": self.ra,
            "dec": self.dec,
            "morph_type": self.morph_type,
            "redshift": self.redshift,
            "size": self.size,
            "model_type": Galaxy.model_type()
        }

    @staticmethod
    def model_type():
        """
        Returns the type of this model.
        The type is defined as the plural form of the class name.
        """
        return "galaxies"

    def __repr__(self):
        """
        Returns a string representation of the Galaxy
        """
        return "<Galaxy %r>" % self.name
