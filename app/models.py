from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Satellite(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    orbital_period = db.Column(db.Float)
    type_of_mission = db.Column(db.String())
    year_launched = db.Column(db.Integer)
    year_decommissioned = db.Column(db.Integer)

    # Relations
    # Satellite has a pointer to its star, planetoid body, and galaxy (should they exist)
    # via backreferences.
    star_id = db.Column(db.Integer, db.ForeignKey('star.id'))
    planetoid_id = db.Column(db.Integer, db.ForeignKey('planetoidbody.id'))
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))

    # Methods
    def __init__(self, name, orbital_period, type_of_mission, year_launched, 
            year_decommissioned = -1):
        # Check types
        assert type(name) is str
        assert type(orbital_period) is float
        assert type(type_of_mission) is str
        assert type(year_launched) is int
        assert type(year_decommissioned) is int

        self.name = name
        self.orbital_period = oribital_period
        self.type_of_mission = type_of_mission
        self.year_launched = year_launched
        self.year_decommissioned = year_decommissioned

    def __repr__(self):
        return "Name: " + self.name +                      \
            "\nOrbital Period: " + self.orbital_period +   \
            "\nType of Mission: " + self.type_of_mission + \
            "\nYear Launched: " + self.year_launched +     \
            "\nYear Decomissioned: " +                     \
                self.year_decomissioned if self.year_decommissioned != -1 else "N/A"


class Star(db.Model):
    # Attributes
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    diameter = db.Column(db.Float)
    images = db.Column(db.String())
    location = db.Column(db.Float)
    age = db.Column(db.Float)
    temperature = db.Column(db.Float)

    # Relations
    # Stars have a pointer to their galaxy via backreference
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))
    planetoid_bodies = db.relationship('PlanetoidBody', backref = 'star', lazy = 'dynamic')
    satellites = db.relationship('Satellite', backref = 'star', lazy = 'dynamic')
    
    # Methods
    def __init__(self, name, diameter, images, location, age, temperature,
            planetoid_bodies = None, satellites = None):
        # Check types
        assert type(name) is str
        assert type(diameter) is float
        assert type(images) is str
        assert type(location) is float
        assert type(age) is float
        assert type(temperature) is float

        self.name = name
        self.diameter = diameter
        self.images = images
        self.location = location
        self.planetoid_bodies = planetoid_bodies
        self.satellites = satellites

    def __str__(self):
        return "Name: " + self.name +        \
            "\nDiameter: " + self.diameter + \
            "\nLocation: " + self.location + \
            "\nAge: " + self.age           + \
            "\nTemperature: " + self.temperature
