#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from flask import Flask, render_template
app = Flask(__name__)

models = {'planetoids': 'Planetoid Bodies', 'stars': 'Stars',
          'galaxies': 'Galaxies', 'satellites': 'Satellites'}

headers = {'planetoids': ["Name", "Diameter", "Images",
                          "Location", "Gravity", "Sol", "Orbital Period", "Age",
                          "Surface Temperatures", "Body it Orbits"],
           'galaxies': ["Name", "Images", "Location", "Age",
                        "Year of Discovery", "Type"],
           'satellites': ["Name", "Orbital Period", "Year Launched",
                          "Year Decommissioned", "Type of Mission"],
           'stars': ["Name", "Diameter", "Images", "Location", "Age",
                     "Temperature", "Type"]}


@app.route("/")
def home():
    return render_template('home.html',
                           title='spacecowboys')


@app.route('/planetoids')
def planetoid_table():
    return render_template('table.html',
                           title='planetoids',
                           model=models['planetoids'],
                           headers=headers['planetoids'],
                           rows=headers['planetoids'])


@app.route('/galaxies')
def galaxies_table():
    return render_template('table.html',
                           title='galaxies',
                           model=models['galaxies'],
                           headers=headers['galaxies'],
                           rows=headers['galaxies'])


@app.route('/satellites')
def satellites_table():
    return render_template('table.html',
                           title='satellites',
                           model=models['satellites'],
                           headers=headers['satellites'],
                           rows=headers['satellites'])


@app.route('/stars')
def stars_table():
    return render_template('table.html',
                           title='stars',
                           model=models['stars'],
                           headers=headers['stars'],
                           rows=headers['stars'])


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
