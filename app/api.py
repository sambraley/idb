import flask_restless
from models import Satellite, Planet, Star, Galaxy, Image

url_prefix = "/api/v1"

def api_setup(flask_app, db) :
    manager = flask_restless.APIManager(flask_app, flask_sqlalchemy_db=db)
    api_setup_satellite(manager)
    api_setup_planet(manager)
    api_setup_star(manager)
    api_setup_galaxy(manager)
    
def api_setup_satellite(manager) :
    blueprint = {
        "model":Satellite,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"satellites",
        "exclude_columns":["planet", "star", "galaxy", "image", "image_pid",
            "year_launched_str"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    manager.create_api(**blueprint)
    
def api_setup_planet(manager) :
    blueprint = {
        "model":Planet,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"planets",
        "exclude_columns":["satellites", "star", "galaxy", "image", "img_pid",
            "diameter_str", "ra_str", "dec_str", "gravity_str", "orbital_period_str",
            "mass_str", "temperature_str"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    manager.create_api(**blueprint)
    
def api_setup_star(manager) :
    blueprint = {
        "model":Star,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"stars",
        "exclude_columns":["satellites", "planets", "galaxy", "image", "img_pid",
            "diameter_str", "ra_str", "dec_str", "mass_str", "temperature_str"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    manager.create_api(**blueprint)
    
def api_setup_galaxy(manager) :
    blueprint = {
        "model":Galaxy,
        "methods":["GET"],
        "url_prefix":url_prefix,
        "collection_name":"galaxies",
        "exclude_columns":["satellites", "planets", "stars", "image", "img_pid",
            "ra_str", "dec_str", "redshift_str", "size_str"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    manager.create_api(**blueprint)
