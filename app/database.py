from models import db, Planet, Satellite, Star, Galaxy
import json

def load_db():

	#Creates tables based on models.py
	db.create_all()

	planets_json = json.loads(open('../data/planets.json').read())
	galaxies_json = json.loads(open('../data/galaxies.json').read())
	satellite_json = json.loads(open('../data/satellites.json').read())
	stars_json = json.loads(open('../data/stars.json').read())

	galaxies = []
	stars = []
	satellites = []
	planets = []

	satellites_fk = {"planet_pids":dict(), "galaxy_pids":dict(), "star_pids":dict()}
	planets_fk = {"galaxy_pids":dict(), "star_pids": dict()}
	stars_fk = dict()

	create_satellite_objs(satellite_json, satellites, satellites_fk)

	create_planet_objs(planets_json, planets, planets_fk, satellites_fk)

	create_star_objs(stars_json, stars, stars_fk, satellites_fk, planets_fk)

	create_galaxy_objs(galaxies_json, galaxies, stars_fk, planets_fk, satellites_fk)

	insert_into_db(galaxies, stars, planets, satellites)

def insert_into_db(*models):
	for table in models:
		for row in table:
			pass
			db.session.add(row)
		db.session.commit()

def create_galaxy_objs(galaxies_json, galaxies, stars_fk, planets_fk, satellites_fk):
	for galaxy in galaxies_json:
		galaxy_pid = galaxy.pop("pid")
		galaxy["galaxy_type"] = galaxy.pop("type") 

		_stars = () if galaxy_pid not in stars_fk else stars_fk[galaxy_pid]
		_satellites = () if galaxy_pid not in satellites_fk["galaxy_pids"] else satellites_fk["galaxy_pids"][galaxy_pid]
		_planets = () if galaxy_pid not in planets_fk["galaxy_pids"] else planets_fk["galaxy_pids"][galaxy_pid]

		galaxies.append(Galaxy(stars = _stars, satellites = _satellites, planets = _planets, **galaxy))


def create_star_objs(stars_json, stars, stars_fk, satellites_fk, planets_fk):
	for star in stars_json:
		star_pid = star.pop("pid")
		galaxy_pid = star.pop("galaxy_pid")

		_satellites = () if star_pid not in satellites_fk["star_pids"] else satellites_fk["star_pids"][star_pid]
		_planets = () if star_pid not in planets_fk["star_pids"] else planets_fk["star_pids"][star_pid]

		star_ref = Star(satellites = _satellites, planets = _planets, **star)
		stars.append(star_ref)

		if galaxy_pid not in stars_fk:
			stars_fk[galaxy_pid] = [star_ref]
		else:
			stars_fk[galaxy_pid].append(star_ref)

def create_planet_objs(planets_json, planets, planets_fk, satellites_fk):
	for planet in planets_json:
		planet_pid = planet.pop("pid")
		galaxy_pid = planet.pop("galaxy_pid")
		star_pid = planet.pop("star_pid")


		if planet_pid in satellites_fk["planet_pids"]:
			planet_ref = Planet(satellites=satellites_fk["planet_pids"][planet_pid], **planet)
		else:
			planet_ref = Planet(**planet)

		planets.append(planet_ref)

		if galaxy_pid not in planets_fk["galaxy_pids"]:
			planets_fk["galaxy_pids"][galaxy_pid] = [planet_ref]
		else:
			planets_fk["galaxy_pids"][galaxy_pid].append(planet_ref)
		
		if star_pid not in planets_fk["star_pids"]:
			planets_fk["star_pids"][star_pid] = [planet_ref]
		else:
			planets_fk["star_pids"][star_pid].append(planet_ref)


def create_satellite_objs(satellite_json, satellites, satellites_fk):
	for sat in satellite_json:
		sat.pop("pid")

		planet_pid = sat.pop("planet_pid")
		galaxy_pid = sat.pop("galaxy_pid")
		star_pid = sat.pop("star_pid")

		#need to make dictionary match name of arguments since you can't name 'type' because keyword
		sat["type_of_mission"] = sat.pop("type")

		satellite_ref = Satellite(**sat)
		satellites.append(satellite_ref)

		if  planet_pid not in satellites_fk["planet_pids"]:
			satellites_fk["planet_pids"][planet_pid] = [satellite_ref]
		else:
			satellites_fk["planet_pids"][planet_pid].append(satellite_ref)

		if galaxy_pid not in satellites_fk["galaxy_pids"]:
			satellites_fk["galaxy_pids"][galaxy_pid] = [satellite_ref]
		else:
			satellites_fk["galaxy_pids"][galaxy_pid].append(satellite_ref)

		if star_pid not in satellites_fk["star_pids"]:
			satellites_fk["star_pids"][star_pid] = [satellite_ref]
		else:
			satellites_fk["star_pids"][star_pid].append(satellite_ref)

load_db()