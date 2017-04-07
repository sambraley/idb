from flask_sqlalchemy import SQLAlchemy
import json
import os

db = SQLAlchemy()
from models import Planet, Star, Satellite, Galaxy

def connect_db(flask_app):
    db_URI = os.getenv('SQLALCHEMY_DATABASE_URI_SPACECOWBOYS')
    if db_URI == None :
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        with flask_app.app_context() : load_db()
    else : # pragma: no cover
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        
    return db

    
def load_db():

    #Creates tables based on models.py
    db.create_all()

    planets_json = json.loads(open('./nasa_scripts/data/planets.json').read())
    galaxies_json = json.loads(open('./nasa_scripts/data/galaxies.json').read())
    satellites_json = json.loads(open('./nasa_scripts/data/satellites.json').read())
    stars_json = json.loads(open('./nasa_scripts/data/stars.json').read())
    
    galaxies = create_galaxy_objs(galaxies_json)
    insert_into_db(galaxies)
    
    stars = create_star_objs(stars_json)
    insert_into_db(stars)
    
    planets = create_planet_objs(planets_json)
    insert_into_db(planets)
    
    satellites = create_satellite_objs(satellites_json)
    insert_into_db(satellites)

def insert_into_db(*models):
    for table in models:
      for row in table:
        pass
        db.session.add(row)
      db.session.commit()

def create_galaxy_objs(galaxies_json):
    galaxies = []
    for galaxy in galaxies_json:
      galaxy_pid = galaxy.pop("pid")
      galaxies.append(Galaxy(**galaxy))
    
    return galaxies

def create_star_objs(stars_json):
    stars = []
    for star in stars_json:
      star_pid = star.pop("pid")
      galaxy_pid = star.pop("galaxy_pid")

      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Star must reside in a galaxy
      
      star_ref = Star(galaxy=host_galaxy, **star)
      stars.append(star_ref)
      
    return stars

def create_planet_objs(planets_json):
    planets = []
    
    for planet in planets_json:
      planet_pid = planet.pop("pid")
      star_pid = planet.pop("star_pid")
      galaxy_pid = planet.pop("galaxy_pid")
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Planet must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Planet must be in a galaxy 
      
      planet_ref = Planet(star=host_star, galaxy=host_galaxy, **planet)
      planets.append(planet_ref)

    return planets

def create_satellite_objs(satellites_json):
    satellites = []
    
    for sat in satellites_json:
      sat.pop("pid")

      planet_pid = sat.pop("planet_pid")
      star_pid = sat.pop("star_pid")
      galaxy_pid = sat.pop("galaxy_pid")
      
      host_planet = Planet.query.get(planet_pid)
      assert host_planet != None # Satellite must orbit a planet
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Satellite must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Satellite must be in a galaxy 
      
      satellite_ref = Satellite(planet=host_planet, star=host_star, galaxy=host_galaxy, **sat)
      satellites.append(satellite_ref)
      
    return satellites
