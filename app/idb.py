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
                'bio': "I'm a senior Computer Science student. I enjoy dancing and coding, but I'm not skilled enough to do both simultaneously."},
               {'name': 'Scott Farrior',  'image': 'sfarrior.jpg',      'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'David Ares',     'image': 'david.jpg',         'commits': 0, 'issues': 0, 'tests': 0,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"}]
about_info = {'commits': 0, 'issues': 0, 'tests': 0}


@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')


@app.route('/planetoids')
def planetoid_table():
    return render_template('table.html',
                           title='Planetoids',
                           model=models['planetoids'],
                           headers=headers['planetoids'],
                           rows=headers['planetoids'])


@app.route('/galaxies')
def galaxies_table():
    return render_template('table.html',
                           title='Galaxies',
                           model=models['galaxies'],
                           headers=headers['galaxies'],
                           rows=headers['galaxies'])


@app.route('/satellites')
def satellites_table():
    return render_template('table.html',
                           title='Satellites',
                           model=models['satellites'],
                           headers=headers['satellites'],
                           rows=headers['satellites'])


@app.route('/stars')
def stars_table():
    return render_template('table.html',
                           title='Stars',
                           model=models['stars'],
                           headers=headers['stars'],
                           rows=headers['stars'])


@app.route("/about")
def about():
    return render_template('about.html',
                           title='About',
                           member_info=member_info,
                           about_info=about_info)


if __name__ == "__main__":
    app.run()
