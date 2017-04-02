#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

from flask import Flask, render_template, jsonify
from database import connect_db, Satellite, Planet, Star, Galaxy

app = Flask(__name__)
connect_db(app, "")

headers = {'planetoids': ["Name", "Diameter", "Gravity", "Temperatures", "Mass", "Orbital Period"],
           'galaxies': ["Name", "Images", "Location", "Age", "Year of Discovery", "Type"],
           'satellites': ["Name", "Orbital Period", "Year Launched", "Year Decommissioned", "Type of Mission"],
           'stars': ["Name", "Diameter", "Images", "Location", "Age", "Temperature", "Type"]}
member_info = [
    {'name': 'Nick Kantor',    'image': 'nick_kantor.png',   'p0_lead': True,  'commits': 20, 'issues': 18, 'tests': 0,  'responsibilities': "Front-End Developer", 'bio': "I'm a Senior Computer Science student and tend to spend my free time playing my trumpet for the longhorn band. After I graduate I plan on pursuing a Master's degree in Computer Science."},
    {'name': 'Samuel Braley',  'image': 'samuel_braley.jpg', 'p0_lead': False, 'commits': 13, 'issues': 0,  'tests': 0,  'responsibilities': "Documentation and Apiary", 'bio': "I am a Computer Science senior with certificates in Business Foundations and Game Design. I enjoy being one of the many Sams in the world and plan on being a programmer manager after I graduate."},
    {'name': 'Taben Malik',    'image': 'taben.jpg', 		     'p0_lead': False, 'commits': 25, 'issues': 0,  'tests': 0,  'responsibilities': "Data Collection and Modeling", 'bio': "A double major in Computer Science and Aerospace Engineering. I am a strong advocate of a Mars mission and hope to be a part of one someday."},
    {'name': 'Gustavo Osorio', 'image': 'gustavo.jpg',       'p0_lead': False, 'commits': 9, 'issues': 0,  'tests': 12, 'responsibilities': "UML Design and Modeling", 'bio': "I'm a senior Computer Science student. I enjoy dancing and coding, but I'm not skilled enough to do both simultaneously."},
    {'name': 'Scott Farrior',  'image': 'sfarrior.jpg',      'p0_lead': False, 'commits': 40, 'issues': 3,  'tests': 0,  'responsibilities': "Server setup/administration and SQLAlchemy backend", 'bio': "I'm a Computer Science major. I work as a TA/Grader as well as Computer Lab technician for the community college, and would like to be an instructor one day."},
    {'name': 'David Ares',     'image': 'david.jpg',         'p0_lead': False, 'commits': 24, 'issues': 0,  'tests': 0,  'responsibilities': "Front-End Developer", 'bio': "I am a non-traditional student with one year of Full-stack web development. Before returning to school, I gained seven years of experience in sales, marketing, and management."}]

about_info = {'commits': 131, 'issues': 21, 'tests': 12}


####################
# Misc. Page Routing
####################
@app.route("/")
def home():
    return render_template('home.html', title='Spacecowboys')

@app.route("/about")
def about():
    return render_template('about.html', title='About', member_info=member_info, about_info=about_info)

@app.route("/report")
def report():
    return render_template('report.html', title='Report')

#####################
# Satellite routing
#####################

@app.route('/satellites')
def satellites_table():
    return render_template('satellites-grid.html', satellites=Satellite.query.all())


@app.route('/satellites/<int:satellite_id>')
def satellite_instance(satellite_id):
    satellite = Satellite.query.get(satellite_id)
    return render_template('satellite.html', satellite=satellite)
    
##################
# Planet routing
##################

@app.route('/planets')
def planet_table():
    return render_template('planets-grid.html', planets=Planet.query.all())

@app.route('/planets/<int:planet_id>')
def planet_instance(planet_id):
    return render_template('planet.html', planet=Planet.query.get(planet_id))

    
##################
# Star routing
##################

@app.route('/stars')
def stars_table():
    return render_template('stars-grid.html', stars=Star.query.all())


@app.route('/stars/<int:star_id>')
def star_instance(star_id):
    return render_template('star.html', star=Star.query.get(star_id))


##################
# Galaxy routing
##################

@app.route('/galaxies')
def galaxies_table():
    return render_template('galaxies-grid.html', galaxies=Galaxy.query.all())


@app.route('/galaxies/<int:galaxy_id>')
def galaxy_instance(galaxy_id):
    return render_template('galaxy.html', galaxy=Galaxy.query.get(galaxy_id))
    
################
# API Routing
################

@app.route('/api/v1/satellites')
def api_satellites(): 
    return jsonify([sat.to_dict() for sat in Satellite.query.all()])

@app.route('/api/v1/satellites/<int:satellite_id>')
def api_satellite(satellite_id) :
    return jsonify(Satellite.query.get_or_404(satellite_id).to_dict())

@app.route('/api/v1/planets')
def api_planets(): 
    return jsonify([planet.to_dict() for planet in Planet.query.all()])

@app.route('/api/v1/planets/<int:planet_id>')
def api_planet(planet_id):
    return jsonify(Planet.query.get_or_404(planet_id).to_dict())

@app.route('/api/v1/stars')
def api_stars():
    return jsonify([star.to_dict() for star in Star.query.all()])
    
@app.route('/api/v1/stars/<int:star_id>')
def api_star(star_id):
    return jsonify(Star.query.get_or_404(star_id).to_dict())

@app.route('/api/v1/galaxies')
def api_galaxies(): 
    return jsonify([galaxy.to_dict() for galaxy in Galaxy.query.all()])
    
@app.route('/api/v1/galaxies/<int:galaxy_id>')
def api_galaxy(galaxy_id):
    return jsonify(Galaxy.query.get_or_404(galaxy_id).to_dict())

@app.errorhandler(404)
def not_found(error) :
    response = jsonify({'code':404, 'message': 'The requested data does not exist'})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()
