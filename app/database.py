from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
from models import Planet, Star, Satellite, Galaxy

# data for database. 1 instance of each
planets_json = [{"diameter": 12742.0,"name": "Earth","orbital_period": 365.0,"mass": 5.972e+24,"dec": 0.0,"temperature": 287,"star_pid": 1,"pid": 1,"ra": 0.0,"galaxy_pid": 1,"gravity": 9.81}]
stars_json = [{"temperature": 5510,"diameter": 1460970.0,"name": "WASP-83","mass": 1.11,"pid": 1,"dec": -19.284243,"ra": 190.152085,"galaxy_pid": 1}]
satellites_json = [{"image": "https://upload.wikimedia.org/wikipedia/en/7/72/MC-2941_Wideband_Global_SATCOM_Satellite.png","year_launched": 2012,"name": "WGS-4 (USA-233)","star_pid": 1,"mission_type": "Communications","info_url": "https://en.wikipedia.org/wiki/Wideband_Global_SATCOM","pid": 1,"planet_pid": 1,"agency": "United Launch Alliance","galaxy_pid": 1}]
galaxies_json = [{"redshift": 0.0,"name": "Milky Way","morph_type": "Spiral","size": 360.0,"pid": 1,"dec": -47.2833,"ra": 17.7533}]

test = True

def connect_db(flask_app, db_URI):
    
    if test :
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        with flask_app.app_context() : load_db()
    else :
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
        db.init_app(flask_app)
        
    return db

    
def load_test_db():
    db.create_all()
    
    galaxies = create_galaxy_objs(galaxies_json)
    insert_into_db(galaxies)
    
    stars = create_star_objs(stars_json)
    insert_into_db(stars)
    
    planets = create_planet_objs(planets_json)
    insert_into_db(planets)
    
    satellites = create_satellite_objs(satellites_json)
    insert_into_db(satellites)
    
    
def load_db():

    #Creates tables based on models.py
    db.create_all()

    planets_json = json.loads(open('./data/planets.json').read())
    galaxies_json = json.loads(open('./data/galaxies.json').read())
    satellites_json = json.loads(open('./data/satellites.json').read())
    stars_json = json.loads(open('./data/stars.json').read())
    
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
