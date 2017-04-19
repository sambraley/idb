from flask_sqlalchemy import SQLAlchemy
import json
import os
from flask_whooshee import Whooshee

db = SQLAlchemy()
whooshee = Whooshee()
from models import Planet, Star, Satellite, Galaxy, Image

def connect_db(flask_app):
    db_URI = os.getenv('SQLALCHEMY_DATABASE_URI_SPACECOWBOYS')
    flask_app.config['WHOOSHEE_MIN_STRING_LEN'] = 1
    
    if db_URI == None :
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        whooshee.init_app(flask_app)
        with flask_app.app_context() as app: 
            load_db()
    else : # pragma: no cover
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        whooshee.init_app(flask_app)
        with flask_app.app_context() as app:
            whooshee.reindex()
        
    return db

    
def load_db():

    #Creates tables based on models.py
    db.create_all()
    
    planets_json = json.loads(open('data/planets.json').read())
    galaxies_json = json.loads(open('data/galaxies.json').read())
    satellites_json = json.loads(open('data/satellites.json').read())
    stars_json = json.loads(open('data/stars.json').read())
    images_json = json.loads(open('data/images.json').read())
    
    images = create_image_objs(images_json)
    insert_into_db(images)
    
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
      
def create_image_objs(images_json):
    images = []
    for image in images_json:
        image_pid = image.pop("pid")
        images.append(Image(**image))
        
    return images

def create_galaxy_objs(galaxies_json):
    galaxies = []
    for galaxy in galaxies_json:
      galaxy_pid = galaxy.pop("pid")
      image_pid = galaxy.pop("image_pid")
      
      image = Image.query.get(image_pid)
      assert image != None # Galaxy must have an image
      
      galaxies.append(Galaxy(image=image, **galaxy))
    
    return galaxies

def create_star_objs(stars_json):
    stars = []
    for star in stars_json:
      star_pid = star.pop("pid")
      galaxy_pid = star.pop("galaxy_pid")
      image_pid = star.pop("image_pid")
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Star must reside in a galaxy
      
      image = Image.query.get(image_pid)
      assert image != None # Star must have an image
      
      star_ref = Star(image=image, galaxy=host_galaxy, **star)
      stars.append(star_ref)
      
    return stars

def create_planet_objs(planets_json):
    planets = []
    
    for planet in planets_json:
      planet_pid = planet.pop("pid")
      star_pid = planet.pop("star_pid")
      galaxy_pid = planet.pop("galaxy_pid")
      image_pid = planet.pop("image_pid")
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Planet must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Planet must be in a galaxy 
      
      image = Image.query.get(image_pid)
      assert image != None # Planet must have an image
      
      planet_ref = Planet(image=image, star=host_star, galaxy=host_galaxy, **planet)
      planets.append(planet_ref)

    return planets

def create_satellite_objs(satellites_json):
    satellites = []
    
    for sat in satellites_json:
      sat.pop("pid")

      planet_pid = sat.pop("planet_pid")
      star_pid = sat.pop("star_pid")
      galaxy_pid = sat.pop("galaxy_pid")
      image_pid = sat.pop("image_pid")
      
      host_planet = Planet.query.get(planet_pid)
      assert host_planet != None # Satellite must orbit a planet
      
      host_star = Star.query.get(star_pid)
      assert host_star != None # Satellite must have a star
      
      host_galaxy = Galaxy.query.get(galaxy_pid)
      assert host_galaxy != None # Satellite must be in a galaxy 
      
      image = Image.query.get(image_pid)
      assert image != None # Satellite must have an image
      
      satellite_ref = Satellite(image=image, planet=host_planet, star=host_star, galaxy=host_galaxy, **sat)
      satellites.append(satellite_ref)
      
    return satellites
