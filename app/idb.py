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
member_info = [{'name': 'Nick Kantor',    'image': 'nick_kantor.png',   'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Front and back end design",
                'bio': "I'm a Senior Computer Science student and tend to spend my free time playing my trumpet for the longhorn band. After I graduate I plan on pursuing a Master's degree in Computer Science."},
               {'name': 'Samuel Braley',  'image': 'samuel_braley.jpg', 'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'Taben Malik',    'image': 'taben.jpg', 		    'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Data Collection and Modeling",
                'bio': "A double major in Computer Science and Aerospace Engineering. I am a strong advocate of a Mars mission and hope to be a part of one someday."},
               {'name': 'Gustavo Osorio', 'image': 'gustavo.jpg',       'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a senior Computer Science student. I enjoy dancing and coding, but I'm not skilled enough to do both simultaneously."},
               {'name': 'Scott Farrior',  'image': 'sfarrior.jpg',      'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"},
               {'name': 'David Ares',     'image': 'david.jpg',         'commits': 5, 'issues': 1, 'tests': 1,
                'responsibilities': "Jack of all trades",
                'bio': "I'm a cuddly wuddly teddy bear"}]
about_info = {'commits': 70, 'issues': 20, 'tests': 2}

planetoids =  [{ "link": "planetoids/1", "name": "HAT-P-33 b", "right_ascension": "113.184212", "declination": "33.835052", "diameter": "235739.892", "mass": "1.446276e+27", "surface_temperature": "1782", "gravity": "0.006947625786270114", "orbital_period": "3.474474", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "HAT-P-33 b.png", "host": "HAT-P-33" },
              { "link": "planetoids/2", "name": "HAT-P-34 b", "right_ascension": "303.195342", "declination": "18.104868", "diameter": "167366.934", "mass": "6.316544e+27", "surface_temperature": "1520", "gravity": "0.06019932261381838", "orbital_period": "5.452654", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "HAT-P-34 b.png", "host": "HAT-P-34"},
              { "link": "planetoids/3", "name": "Kepler-117 b", "right_ascension": "288.793037", "declination": "48.040234", "diameter": "100532.018", "mass": "1.7841199999999998e+26", "surface_temperature": "984", "gravity": "0.0047126659923379345", "orbital_period": "18.7959228", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "Kepler-117 b.png", "host": "Kepler-117"} ]

stars = [{ "link": "stars/1","name": "HAT-P-33", "diameter": "NULL", "distance": "NULL", "mass": "1.38", "temperature": "6446.0", "right_ascension": "303.195342", "declination": "33.835052", "images": "HAT-P-33.png"},
        { "link": "stars/2", "name": "HAT-P-34", "diameter": "NULL", "distance": "NULL", "mass": "1.39", "temperature": "6442.0", "right_ascension": "113.184212", "declination": "18.104868", "images": "HAT-P-34.png"},
        { "link": "stars/3", "name": "Kepler-117", "diameter": "NULL", "distance": "NULL", "mass": "1.13", "temperature": "6150.0", "right_ascension": "288.793037", "declination": "48.040234", "images": "Kepler-117.png"}]

satellites = [ { "link": "satellites/1", "name": "WGS-4 (USA-233)", "agency": "United Launch Alliance", "type_of_mission": "communications", "year_launched": "2012", "oribital_period": "NULL", "images": ""}, 
               { "link": "satellites/2", "name": "Nuclear Spectroscopic Telescope Array (NuSTAR)", "agency": "National Aeronautics and Space Administration", "type_of_mission": "astrophysics", "year_launched": "2012", "oribital_period": "NULL", "images": ""}, 
               { "link": "satellites/3", "name": "SARAL", "agency": "Indian Space Research Organization", "type_of_mission": "planetary science", "year_launched": "2013", "oribital_period": "NULL", "images": ""} ]

galaxies = [{ "link": "galaxies/1", "name": "UGC 11693", "images": "UGC 11693.png", "right_ascension":"317.819183", "declination":"37.884811", "galaxy_type":"spiral", "redshift":"0.093554", "angular_size": "1.227", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"},
            { "link": "galaxies/2", "name": "UGC 11822", "images": "UGC 11822.png", "right_ascension":"327.418700", "declination":"40.663325", "galaxy_type":"barred spiral", "redshift":"0.014739", "angular_size": "1.170", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"},
            { "link": "galaxies/3", "name": "UGC 11891", "images": "UGC 11891.png", "right_ascension":"330.8908", "declination":"43.7492", "galaxy_type": "irregular", "redshift":"0.001538", "angular_size": "4.0", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"}]

@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')

@app.route('/planetoids')
def planetoid_table():
    return render_template('planetoids-grid.html', planetoid=planetoids)

@app.route('/planetoids/<int:planetoid_id>')
def planetoid_instance(planetoid_id) :
    return render_template('planetoid.html', planetoid=planetoids[planetoid_id - 1])



@app.route('/galaxies')
def galaxies_table():
    return render_template('galaxies-grid.html', galaxies=galaxies)

@app.route('/galaxies/<int:galaxy_id>')
def galaxy_instance(galaxy_id) :
    return render_template('galaxy.html', galaxy=galaxies[galaxy_id - 1])



@app.route('/satellites')
def satellites_table():
    return render_template('satellites-grid.html', satellite=satellites)

@app.route('/satellites/<int:satellite_id>')
def satellite_instance(satellite_id):
    return render_template('satellite.html', satellite=satellites[satellite_id - 1])


@app.route('/stars')
def stars_table():
    return render_template('stars-grid.html', star=stars)

@app.route('/stars/<int:star_id>')
def star_instance(star_id):
    return render_template('star.html', star=stars[star_id - 1])


@app.route("/about")
def about():
    return render_template('about.html',
                           title='About',
                           member_info=member_info,
                           about_info=about_info)


if __name__ == "__main__":
    app.run()
