from flask import Flask, render_template
app = Flask(__name__)

models = {'planetoid': 'Planetoid Bodies', 'stars': 'Stars', 
		'galaxies': 'Galaxies', 'satellites': 'Satellites'}

headers = {'planetoid': ["Name", "Diameter", "Images", 
    "Location", "Gravity", "Sol", "Orbital Period", "Age", 
    "Surface Temperatures", "Body it Orbits"],
    'galaxies': ["Name", "Images", "Location", "Age", 
    "Year of Discovery", "Type" ],
    'satellites': ["Name", "Orbital Period", "Year Launched", 
    "Year Decommissioned", "Type of Mission"],
    'stars': ["Name", "Diameter", "Images", "Location", "Age", 
    "Temperature", "Type"] }

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/planetoid')
def planetoid_table():
    return render_template('table.html',
                           title='planetoid',
                           model=models['planetoid'],
                           headers= headers['planetoid'] )

@app.route('/galaxies')
def galaxies_table():
    return render_template('table.html',
                           title='galaxies',
                           model=models['galaxies'],
                           headers= headers['galaxies'] )

@app.route('/satellites')
def satellites_table():
    return render_template('table.html',
                           title='satellites',
                           model=models['satellites'],
                           headers= headers['satellites'] )

@app.route('/stars')
def stars_table():
    return render_template('table.html',
                           title='stars',
                           model=models['stars'],
                           headers= headers['stars'] )

if __name__ == "__main__":
    app.run()
