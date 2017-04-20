#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

import io
import unittest
import test
from lib.search_db import search
from flask import Flask, render_template, request, jsonify
from database import connect_db, Satellite, Planet, Star, Galaxy
from api import api_setup

app = Flask(__name__)
db = connect_db(app)
api_setup(app, db)

def in_solar_system(name):
    return (name == "Mercury" or
            name == "Venus" or
            name == "Earth" or
            name == "Mars" or
            name == "Jupiter" or
            name == "Saturn" or
            name == "Uranus" or
            name == "Neptune" or
            name == "Pluto" or
            name == "Sun")

####################
# Misc. Page Routing
####################
@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')

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
    # earth
    planet = Planet.query.get(planet_id)
    planet_name = planet.to_dict()["name"]
    if in_solar_system(planet_name):
        return render_template('sol.html', planet=planet)
    return render_template('planet.html', planet=planet)

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
    star = Star.query.get(star_id)
    star_name = star.to_dict()["name"]
    if in_solar_system(star_name):
        return render_template('sol_star.html', star=star)
    return render_template('star.html', star=star)


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
    suite = unittest.TestLoader().loadTestsFromTestCase(test.TestModels)
    test_output = io.StringIO()
    unittest.TextTestRunner(stream=test_output).run(suite)
    test_output = test_output.getvalue()
    coverage = open("coverage.txt")
    coverage_output = coverage.read()
    output = test_output + "\n" + coverage_output
    return output

@app.route('/search')
def search_page():
    return render_template('search.html', title='search')

@app.route('/visualization')
def visualize():
    script = "/static/js/" + request.args["graph"] + ".js"
    return render_template('visualization.html', title='visualization', script=script)

@app.route('/api/v1/search')
def search_api():
    output = search(request.args)
    return jsonify(output)

if __name__ == "__main__": # pragma: no cover
    app.run()
