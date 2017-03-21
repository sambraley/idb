from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Satellite(db.Model):
    # Attributes
    name = db.Column(db.String(), primary_key = True)
    orbital_period = db.Column(db.Float)
    type_of_mission = db.Column(db.String())
    year_launched = db.Column(db.Integer)
    year_decommissioned = db.Column(db.Integer, nullable = True)

    # Relations
    # Satellite has a pointer to its star, planetoid body, and galaxy (should they exist)
    # via backreferences.

    # Methods
    def __init__(self, name, orbital_period, type_of_mission, year_launched, 
            year_decommissioned = None):
        # Check types
        assert type(name) is str
        assert type(orbital_period) is float
        assert type(type_of_mission) is str
        assert type(year_launched) is int
        assert type(year_decommissioned) is int or type(year_decommissioned) is None

        self.name = name
        self.orbital_period = oribital_period
        self.type_of_mission = type_of_mission
        self.year_launched = year_launched
        self.year_decommissioned = year_decommissioned

    def __str__(self):
        print("Name:", self.name)
        print("Orbital Period:", self.orbital_period)
        print("Type of Mission:", self.type_of_mission)
        print("Year Launched:", self.year_launched)
        print("Year Decomissioned:", 
                self.year_decomissioned if year_decommissioned is not None else "N/A")
