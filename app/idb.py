#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from flask import Flask, render_template
app = Flask(__name__)

models = {'planetoids': 'Planetoid Bodies', 'stars': 'Stars',
          'galaxies': 'Galaxies', 'satellites': 'Satellites'}

headers = {'planetoids': ["Name", "Diameter", "Gravity", "Temperatures", "Mass",
                           "Orbital Period"],
           'galaxies': ["Name", "Images", "Location", "Age",
                        "Year of Discovery", "Type"],
           'satellites': ["Name", "Orbital Period", "Year Launched",
                          "Year Decommissioned", "Type of Mission"],
           'stars': ["Name", "Diameter", "Images", "Location", "Age",
                     "Temperature", "Type"]}
member_info = [{'name': 'Nick Kantor',    'image': 'nick_kantor.png',   'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a Senior Computer Science student and tend to spend my free time playing my trumpet for the longhorn band. After I graduate I plan on pursuing a Master's degree in Computer Science."},
               {'name': 'Samuel Braley',  'image': 'samuel_braley.jpg', 'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'Taben Malik',    'image': 'taben.jpg', 		    'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Data Collection and Modeling",
                'bio': "A double major in Computer Science and Aerospace Engineering. I am a strong advocate of a Mars mission and hope to be a part of one someday."},
               {'name': 'Gustavo Osorio', 'image': 'gustavo.jpg',       'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'Scott Farrior',  'image': 'sfarrior.jpg',      'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'David Ares',     'image': 'david.jpg',         'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"}]

planetoid =  {"HAT-P-33-b": {"name": "HAT-P-33 b", "right_ascension": "113.184212", "declination": "33.835052", "diameter": "235739.892", "mass": "1.446276e+27", "surface_temperature": "1782", "gravity": "0.006947625786270114", "orbital_period": "NULL", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "HAT-P-33 b.png" } }
star = {"HAT-P-33" : {"name": "HAT-P-33", "diameter": "NULL", "distance": "NULL", "mass": "1.38", "temperature": "6446.0", "right_ascension": "113.184212", "declination": "33.835052", "images": "HAT-P-33.png"}}



@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')


@app.route('/planetoids')
def planetoid_table():
    return render_template('planetoids-grid.html')

@app.route('/HAT-P-33-b')
def planetoid_model():
    return render_template('planetoid.html', planetoid=planetoid["HAT-P-33-b"])

@app.route('/galaxies')
def galaxies_table():
    return render_template('galaxies-grid.html')

@app.route('/UGC-11693')
def galaxies_model():
    return render_template('galaxy.html')


@app.route('/satellites')
def satellites_table():
    return render_template('satellites-grid.html')

@app.route('/WGS-4-USA-233')
def satellites_model():
    return render_template('satellite.html')


@app.route('/stars')
def stars_table():
    return render_template('stars-grid.html')

@app.route('/HAT-P-33')
def stars_model():
    return render_template('star.html', star= star["HAT-P-33"])

@app.route("/about")
def about():
    return render_template('about.html',
                           title='About',
                           member_info=member_info)


if __name__ == "__main__":
    app.run()
