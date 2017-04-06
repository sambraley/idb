#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long
from flask import Flask, render_template

from database import connect_db, Satellite, Planet, Star, Galaxy
from api import api_setup
import subprocess

app = Flask(__name__)
db = connect_db(app)
api_setup(app, db)

headers = {'planetoids': ["Name", "Diameter", "Gravity", "Temperatures", "Mass", "Orbital Period"],
           'galaxies': ["Name", "Images", "Location", "Age", "Year of Discovery", "Type"],
           'satellites': ["Name", "Orbital Period", "Year Launched", "Year Decommissioned", "Type of Mission"],
           'stars': ["Name", "Diameter", "Images", "Location", "Age", "Temperature", "Type"]}


####################
# Misc. Page Routing
####################
@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')


@app.route('/planetoids/<int:planetoid_id>')
def planetoid_instance(planetoid_id):
    return render_template('planetoid.html', planetoid=planetoids[planetoid_id - 1])


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/report")
def report():
    return render_template('report.html', title='Report')

#####################
# Satellite routing
#####################

@app.route('/satellites')
def satellites_table():
    return render_template('models_grid.html', title="Satellites")

# @app.route('/satellites')
# def satellites_table():
#     return render_template('satellites-grid.html', satellites=Satellite.query.all())


@app.route('/satellites/<int:satellite_id>')
def satellite_instance(satellite_id):
    satellite = Satellite.query.get(satellite_id)
    return render_template('satellite.html', satellite=satellite)

##################
# Planet routing
##################

@app.route('/planets')
def planets_table():
    return render_template('models_grid.html', title="Planets")

# @app.route('/planets')
# def planet_table():
#     return render_template('planets-grid.html', planets=Planet.query.all())

@app.route('/planets/<int:planet_id>')
def planet_instance(planet_id):
    return render_template('planet.html')

# return render_template('planet.html', planet=Planet.query.get(planet_id))

##################
# Star routing
##################

@app.route('/stars')
def stars_table():
    return render_template('models_grid.html', title="Stars")

# @app.route('/stars')
# def stars_table():
#     return render_template('stars-grid.html', stars=Star.query.all())


@app.route('/stars/<int:star_id>')
def star_instance(star_id):
    return render_template('star.html', star=Star.query.get(star_id))


##################
# Galaxy routing
##################

@app.route('/galaxies')
def galaxies_table():
    return render_template('models_grid.html', title="Galaxies")


@app.route('/galaxies/<int:galaxy_id>')
def galaxy_instance(galaxy_id):
    return render_template('galaxy.html', galaxy=Galaxy.query.get(galaxy_id))

@app.route('/run_tests')
def run_tests():
		output = subprocess.check_output(["python3", "app/test.py"], stderr=subprocess.STDOUT)
		output = output.decode("utf-8")
		output = "<pre style='font-family: Courier New;'>" + output + "</pre>"
		return output


if __name__ == "__main__": # pragma: no cover
    app.run()
