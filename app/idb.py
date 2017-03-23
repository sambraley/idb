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

planetoid =  [{ "link": "HAT-P-33-b", "name": "HAT-P-33 b", "right_ascension": "113.184212", "declination": "33.835052", "diameter": "235739.892", "mass": "1.446276e+27", "surface_temperature": "1782", "gravity": "0.006947625786270114", "orbital_period": "3.474474", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "HAT-P-33 b.png", "host": "HAT-P-33" },
              { "link": "HAT-P-34-b", "name": "HAT-P-34 b", "right_ascension": "303.195342", "declination": "18.104868", "diameter": "167366.934", "mass": "6.316544e+27", "surface_temperature": "1520", "gravity": "0.06019932261381838", "orbital_period": "5.452654", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "HAT-P-34 b.png", "host": "HAT-P-34"},
              { "link": "Kepler-117-b", "name": "Kepler-117 b", "right_ascension": "288.793037", "declination": "48.040234", "diameter": "100532.018", "mass": "1.7841199999999998e+26", "surface_temperature": "984", "gravity": "0.0047126659923379345", "orbital_period": "18.7959228", "orbiting_bodies": "NULL", "satellites": "NULL", "images": "Kepler-117 b.png", "host": "Kepler-117"} ]

star = [{ "link": "HAT-P-33","name": "HAT-P-33", "diameter": "NULL", "distance": "NULL", "mass": "1.38", "temperature": "6446.0", "right_ascension": "303.195342", "declination": "33.835052", "images": "HAT-P-33.png"},
        { "link": "HAT-P-34", "name": "HAT-P-34", "diameter": "NULL", "distance": "NULL", "mass": "1.39", "temperature": "6442.0", "right_ascension": "113.184212", "declination": "18.104868", "images": "HAT-P-34.png"},
        { "link": "Kepler-117", "name": "Kepler-117", "diameter": "NULL", "distance": "NULL", "mass": "1.13", "temperature": "6150.0", "right_ascension": "288.793037", "declination": "48.040234", "images": "Kepler-117.png"}]

satellite = [ { "link": "USA-233", "name": "WGS-4 (USA-233)", "agency": "United Launch Alliance", "type_of_mission": "communications", "year_launched": "2012", "oribital_period": "NULL"}, 
              { "link": "NuSTAR", "name": "Nuclear Spectroscopic Telescope Array (NuSTAR)", "agency": "National Aeronautics and Space Administration", "type_of_mission": "astrophysics", "year_launched": "2012", "oribital_period": "NULL"}, 
              { "link": "SARAL", "name": "SARAL", "agency": "Indian Space Research Organization", "type_of_mission": "planetary science", "year_launched": "2013", "oribital_period": "NULL"} ]

galaxies = [{ "link": "UGC-11693", "name": "UGC 11693", "images": "UGC 11693.png", "right_ascension":"317.819183", "declination":"37.884811", "galaxy_type":"spiral", "redshift":"0.093554", "angular_size": "1.227", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"},
            { "link": "UGC-11822", "name": "UGC 11822", "images": "UGC 11822.png", "right_ascension":"327.418700", "declination":"40.663325", "galaxy_type":"barred spiral", "redshift":"0.014739", "angular_size": "1.170", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"},
            { "link": "UGC-11891", "name": "UGC 11891", "images": "UGC 11891.png", "right_ascension":"330.8908", "declination":"43.7492", "galaxy_type": "irregular", "redshift":"0.001538", "angular_size": "4.0", "stars": "/stars", "planetoid_bodies": "/planetoids", "satellites": "/satellites"}]

@app.route("/")
def home():
    return render_template('home.html',
                           title='Spacecowboys')

@app.route('/planetoids')
def planetoid_table():
    return render_template('planetoids-grid.html', planetoid=planetoid)

@app.route('/HAT-P-33-b')
def planetoid_model1():
    return render_template('planetoid.html', planetoid=planetoid[0])

@app.route('/HAT-P-34-b')
def planetoid_model2():
    return render_template('planetoid.html', planetoid=planetoid[1])

@app.route('/Kepler-117-b')
def planetoid_model3():
    return render_template('planetoid.html', planetoid=planetoid[2])


@app.route('/galaxies')
def galaxies_table():
    return render_template('galaxies-grid.html', galaxies=galaxies)

@app.route('/UGC-11693')
def galaxies_model1():
    return render_template('galaxy.html', galaxy=galaxies[0])

@app.route('/UGC-11822')
def galaxies_model2():
    return render_template('galaxy.html', galaxy=galaxies[1])

@app.route('/UGC-11891')
def galaxies_model3():
    return render_template('galaxy.html', galaxy=galaxies[2])


@app.route('/satellites')
def satellites_table():
    return render_template('satellites-grid.html', satellite=satellite)

@app.route('/USA-233')
def satellites_model1():
    return render_template('satellite.html', satellite=satellite[0])

@app.route('/NuSTAR')
def satellites_model2():
    return render_template('satellite.html', satellite=satellite[1])

@app.route('/SARAL')
def satellites_model3():
    return render_template('satellite.html', satellite=satellite[2])


@app.route('/stars')
def stars_table():
    return render_template('stars-grid.html', star=star)

@app.route('/HAT-P-33')
def stars_model1():
    return render_template('star.html', star= star[0])

@app.route('/HAT-P-34')
def stars_model2():
    return render_template('star.html', star= star[1])

@app.route('/Kepler-117')
def stars_model3():
    return render_template('star.html', star= star[2])


@app.route("/about")
def about():
    return render_template('about.html',
                           title='About',
                           member_info=member_info)


if __name__ == "__main__":
    app.run()
