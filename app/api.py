import flask_restless
from models import Satellite, Planet, Star, Galaxy

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
        "exclude_columns":["planet", "star", "galaxy"],
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
        "exclude_columns":["satellites", "star", "galaxy"],
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
        "exclude_columns":["satellites", "planets", "galaxy"],
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
        "exclude_columns":["satellites", "planets", "stars"],
        "results_per_page":9,
        "max_results_per_page":50
    }
    
    manager.create_api(**blueprint)