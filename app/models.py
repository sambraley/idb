from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models artifical satellites
class Satellite(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    agency = db.Column(db.String())
    type_of_mission = db.Column(db.String())
    year_launched = db.Column(db.Integer)
    orbital_period = db.Column(db.Float)

    # Relations
    # Satellite has a pointer to its star, planetoid body, and galaxy (should they exist)
    # via backreferences.
    
    # We have at most one of each of these
    star_id = db.Column(db.Integer, db.ForeignKey('star.id'))
    planetoid_id = db.Column(db.Integer, db.ForeignKey('planetoid_body.id'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))

    # Methods
    def __init__(self, name, agency, type_of_mission, year_launched, orbital_period):
        # Check types
        assert type(name) is str
        assert type(agency) is str
        assert type(type_of_mission) is str
        assert type(year_launched) is int
        assert type(orbital_period) is float

        self.name = name
        self.agency = agency
        self.type_of_mission = type_of_mission
        self.year_launched = year_launched
        self.orbital_period = oribital_period

    def __repr__(self):
        return "Name: " + self.name +                      \
            "\nAgency: " + self.agency +                   \
            "\nType of Mission: " + self.type_of_mission + \
            "\nYear Launched: " + self.year_launched +     \
            "\nOrbital Period: " + self.orbital_period

class Star(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    images = db.Column(db.String())
    temperature = db.Column(db.Float)
    diameter = db.Column(db.Float)
    right_ascension = db.Column(db.Float)
    declination = db.Column(db.Float)
    mass = db.Column(db.Float)
    distance = db.Column(db.Float)

    # Relations
    # Stars have a pointer to their galaxy via backreference
    
    # We have at most one of these
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))
    
    # We could have many of these
    planetoid_bodies = db.relationship('PlanetoidBody', backref = 'star', lazy = 'dynamic')
    satellites = db.relationship('Satellite', backref = 'star', lazy = 'dynamic')
    
    # Methods
    # planetoid_bodies and satellites are to be iterables containing instances of the respective
    # classes which orbit this star
    def __init__(self, name, images, temperature, diameter, right_ascension, declination, mass,
            distance, planetoid_bodies = None, satellites = None):
        # Check types
        assert type(name) is str
        assert type(images) is str
        assert type(temperature) is float
        assert type(diameter) is float
        assert type(right_ascension) is float
        assert type(declination) is float
        assert type(mass) is float
        assert type(distance) is float

        self.name = name
        self.images = images
        self.temperature = temperature
        self.diameter = diameter
        self.right_ascension = right_ascension
        self.declination = declination
        self.mass = mass
        self.distance = distance
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

    def __repr__(self):
        return "Name: " + self.name +                      \
            "\nTemperature: " + self.temperature +         \
            "\nDiameter: " + self.diameter +               \
            "\nRight Ascension: " + self.right_ascension + \
            "\nDeclination: " + self.declination +         \
            "\nMass: " + self.mass +                       \
            "\nDistance: " + self.distance

class Galaxy(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    images = db.Column(db.String())
    right_ascension = db.Column(db.Float)
    declination = db.Column(db.Float)
    galaxy_type = db.Column(db.String())
    redshift = db.Column(db.Float)
    angular_size = db.Column(db.Float)

    # Relations

    # We could have many of all of these
    stars = db.relationship('Star', backref = 'galaxy', lazy = 'dynamic')
    planetoid_bodies = db.relationship('PlanetoidBody', backref = 'galaxy', lazy = 'dynamic')
    satellites = db.relationship('Satellite', backref = 'galaxy', lazy = 'dynamic')
    
    # Methods
    # stars, planetoid_bodies, and satellites are to be iterables containing instances 
    # of the respective classes which are within this galaxy
    def __init__(self, name, images, right_ascension, declination, galaxy_type, redshift, 
            angular_size, stars = None, planetoid_bodies = None, satellites = None):
        # Check types
        assert type(name) is str
        assert type(images) is str
        assert type(right_ascension) is float
        assert type(declination) is float
        assert type(galaxy_type) is str
        assert type(redshift) is float
        assert type(angular_size) is float

        self.name = name
        self.images = images
        self.right_ascension = right_ascension
        self.declination = declination
        self.galaxy_type = galaxy_type
        self.redshift = redshift
        self.angular_size = angular_size
        self.stars = stars
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

    def __repr__(self):
        return "Name: " + self.name +                      \
            "\nRight Ascension: " + self.right_ascension + \
            "\nDeclination: " + self.declination +         \
            "\nGalaxy Type: " + self.galaxy_type +         \
            "\nRedshift: " + self.redshift +               \
            "\nAngular Size: " + self.angular_size         

# Planets, moons, comets, asteroids ...
class PlanetoidBody(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, unique = True)
    images = db.Column(db.String())
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
    host_id = db.Column(db.Integer, db.ForeignKey('planetoid_body.id'))
    star_id = db.Column(db.Integer, db.ForeignKey('star.id'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))
    
    # We could have many of these
    orbiting_bodies = db.relationship('PlanetoidBody', backref = 'host', lazy = 'dynamic')
    satellites = db.relationship('Satellite', backref = 'planetoid_body', lazy = 'dynamic')

    # Methods
    # orbiting_bodies, and satellites are to be iterables containing instances of the respective 
    # classes which are within this galaxy
    def __init__(self, name, images, diameter, surface_temperature, right_ascension, declination, 
            mass, gravity, orbital_period, orbiting_bodies = None, satellites = None):
        # Check types
        assert type(name) is str
        assert type(images) is str
        assert type(diameter) is float
        assert type(surface_temperature) is float
        assert type(right_ascension) is float
        assert type(declination) is float
        assert type(mass) is float
        assert type(gravity) is str
        assert type(orbital_period) is float
        
        self.name = name
        self.images = images
        self.diameter = diameter
        self.surface_temperature = surface_temperature
        self.right_ascension = right_ascension
        self.declination = declination
        self.mass = mass
        self.gravity = gravity
        self.orbital_period = orbital_period
        self.orbiting_bodies = orbiting_bodies
        self.satellites = satellites

    def __repr__(self):
        return "Name: " + self.name +                               \
            "\nDiameter: " + self.diameter +                        \
            "\nSurface Temperature: " + self.surface_temperature +  \
            "\nRight Ascension: " + self.right_ascension +          \
            "\nDeclination: " + self.declination +                  \
            "\nMass: " + self.mass +                                \
            "\nGravity: " + self.gravity +                          \
            "\nOrbital Period: " + self.orbital_period
