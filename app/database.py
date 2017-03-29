from models import db, PlanetoidBody, Satellite, Star, Galaxy
import json

def load_db():
	planets = json.loads(open('../nasa_scripts/planets.json').read())
	galaxies = json.loads(open('../nasa_scripts/galaxies.json').read())
	satellites = json.loads(open('../nasa_scripts/satellites.json').read())
	stars = json.loads(open('../nasa_scripts/stars.json').read())

	db.create_all()

	for row in planets:
		current = PlanetoidBody(**row)
		db.session.add(current)

	for row in galaxies:
		current = Galaxy(**row)
		db.session.add(current)

	for row in satellites:
		current = Satellite(**row)
		db.session.add(current)

	for row in stars:
		current = Star(**row)
		db.session.add(current)

	db.session.commit()

