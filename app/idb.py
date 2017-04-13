#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long
import io
import unittest
import test
from flask import Flask, render_template, request
from database import connect_db, Satellite, Planet, Star, Galaxy
from api import api_setup

app = Flask(__name__)
db = connect_db(app)
api_setup(app, db)


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
    if (planet_id == 299):
        return render_template('earth.html', planet=Planet.query.get(planet_id))
    return render_template('planetoid.html', planet=Planet.query.get(planet_id))

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
    suite = unittest.TestLoader().loadTestsFromTestCase(test.TestModels)
    test_output = io.StringIO()
    unittest.TextTestRunner(stream=test_output).run(suite)
    test_output = test_output.getvalue()
    coverage = open("coverage.txt")
    coverage_output = coverage.read()
    output = "<pre>" + test_output + "\n" + coverage_output + "</pre>"
    return output

@app.route('/search')
def search():
    q = request.args.get('q')
    results = []
    if q != None:
        satellites = Satellite.query.whooshee_search(q)
        planets = Planet.query.whooshee_search(q)
        stars = Star.query.whooshee_search(q)
        galaxies = Galaxy.query.whooshee_search(q)
        results.append(satellites.all())
        results.append(planets.all())
        results.append(stars.all())
        results.append(galaxies.all())
    
    return render_template('search.html', title="search", results=results)

if __name__ == "__main__": # pragma: no cover
    app.run()
