#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = import-error
# pylint: disable = too-many-public-methods

from unittest import main, TestCase
from flask import Flask
from idb import app
from test_models import test_db, Satellite, Star, Galaxy, Planet, Image

test_app = Flask(__name__)
test_app.config["SQLACLHEMY_DATABASE_URI"] = "sqlite:///:memory:"
test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
test_db.init_app(test_app)

with test_app.app_context():
    test_db.create_all()

star_data = {"name": "dummy_star", "temperature": 5945, "mass": 1.09, "diameter": 1405314.0,
             "dec": -5.086445, "ra": 102.721137}

planet_data = {"name": "dummy_planet", "orbital_period": 1.327347, "temperature": 1823,
               "mass": 3.477136e+27, "diameter": 176735.008, "gravity": 0.029718570060615346,
               "dec": 44.915352, "ra": 188.266255}

satellite_data = {"name": "dummy_satellite", "mission_type": "Planetary Science",
                  "info_url": "https://en.wikipedia.org/wiki/SARAL", "agency":
                  "Indian Space Research Organization", "year_launched": 2013}

galaxy_data = {"name": "dummy_galaxy", "morph_type": "Spiral", "size": 1.227, "dec": 37.884811,
               "ra": 317.819183, "redshift": 0.027192}

img_data = {"img_url": "URL"}


class TestModels(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get("/about")
        self.assertEqual(result.status_code, 200)

    def test_report_status_code(self):
        result = self.app.get("/report")
        self.assertEqual(result.status_code, 200)

    def test_satellites_status_code(self):
        result = self.app.get("/satellites")
        self.assertEqual(result.status_code, 200)

    def test_satellites_instance_status_code(self):
        result = self.app.get("/satellites/1")
        self.assertEqual(result.status_code, 200)

    def test_planets_status_code(self):
        result = self.app.get("/planets")
        self.assertEqual(result.status_code, 200)

    def test_planets_instance_status_code(self):
        result = self.app.get("/planets/1")
        self.assertEqual(result.status_code, 200)

    def test_stars_status_code(self):
        result = self.app.get("/stars")
        self.assertEqual(result.status_code, 200)

    def test_stars_instance_status_code(self):
        result = self.app.get("/stars/1")
        self.assertEqual(result.status_code, 200)

    def test_galaxies_status_code(self):
        result = self.app.get("/galaxies")
        self.assertEqual(result.status_code, 200)

    def test_galaxies_instance_status_code(self):
        result = self.app.get("/galaxies/1")
        self.assertEqual(result.status_code, 200)

    def test_search_status_code(self):
        result = self.app.get("/search")
        self.assertEqual(result.status_code, 200)

    def test_visualization_status_code(self):
        result = self.app.get("/visualization")
        self.assertEqual(result.status_code, 200)

    def test_galaxy_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)

        actual = galaxy.to_dict()

        for k, v in galaxy_data.items():
            self.assertEqual(actual[k], v)

    def test_galaxy_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            actual = galaxy.to_dict()

            for k, v in galaxy_data.items():
                self.assertEqual(actual[k], v)

            test_db.session.delete(galaxy)
            test_db.session.commit()

            """
            Check to make sure row got deleted
            """
            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)

    def test_galaxy_repr(self):
        """
        Checks model's correct representation is returned.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)

        actual = repr(galaxy)
        expected = "<Galaxy 'dummy_galaxy'>"
        self.assertEqual(actual, expected)

    def test_star_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)

        actual = star.to_dict()

        for k, v in star_data.items():
            self.assertEqual(actual[k], v)

    def test_star_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            actual = star.to_dict()

            for k, v in star_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(star.galaxy_pid, galaxy.pid)

            test_db.session.delete(star)
            test_db.session.delete(galaxy)
            test_db.session.commit()

            """
            Check to make sure row got deleted
            """
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)

    def test_star_repr(self):
        """
        Checks model's correct representation is returned.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)

        actual = repr(star)
        expected = "<Star 'dummy_star'>"
        self.assertEqual(actual, expected)

    def test_planet_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)

        actual = planet.to_dict()

        for k, v in planet_data.items():
            self.assertEqual(actual[k], v)

    def test_planet_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            planet = test_db.session.query(Planet).filter_by(
                name="dummy_planet").first()

            actual = planet.to_dict()

            for k, v in planet_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(planet.star_pid, star.pid)
            self.assertEqual(planet.galaxy_pid, galaxy.pid)

            test_db.session.delete(star)
            test_db.session.delete(galaxy)
            test_db.session.delete(planet)
            test_db.session.commit()

            """
            Check to make sure row got deleted
            """
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet = test_db.session.query(Planet).filter_by(
                name="dummy_planet").first()
            self.assertEqual(planet, None)

    def test_planet_repr(self):
        """
        Checks model's correct representation is returned.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)

        actual = repr(planet)
        expected = "<Planet 'dummy_planet'>"
        self.assertEqual(actual, expected)

    def test_satellite_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)
        satellite = Satellite(image=img, galaxy=galaxy,
                              star=star, planet=planet, **satellite_data)

        actual = satellite.to_dict()

        for k, v in satellite_data.items():
            self.assertEqual(actual[k], v)

    def test_satellite_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)
        satellite = Satellite(image=img, galaxy=galaxy,
                              star=star, planet=planet, **satellite_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.add(planet)
            test_db.session.add(satellite)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            planet = test_db.session.query(Planet).filter_by(
                name="dummy_planet").first()
            satellite = test_db.session.query(Satellite).filter_by(
                name="dummy_satellite").first()

            actual = satellite.to_dict()

            for k, v in satellite_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(satellite.galaxy_pid, galaxy.pid)
            self.assertEqual(satellite.star_pid, star.pid)
            self.assertEqual(satellite.planet_pid, planet.pid)

            test_db.session.delete(star)
            test_db.session.delete(galaxy)
            test_db.session.delete(planet)
            test_db.session.delete(satellite)
            test_db.session.commit()

            """
            Check to make sure row got deleted
            """
            star = test_db.session.query(Star).filter_by(
                name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy = test_db.session.query(Galaxy).filter_by(
                name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet = test_db.session.query(Planet).filter_by(
                name="dummy_planet").first()
            self.assertEqual(planet, None)
            satellite = test_db.session.query(Satellite).filter_by(
                name="dummy_satellite").first()
            self.assertEqual(satellite, None)

    def test_satellite_repr(self):
        """
        Checks model's correct representation is returned.
        """
        img = Image(**img_data)
        galaxy = Galaxy(image=img, **galaxy_data)
        star = Star(image=img, galaxy=galaxy, **star_data)
        planet = Planet(image=img, galaxy=galaxy, star=star, **planet_data)
        satellite = Satellite(image=img, galaxy=galaxy,
                              star=star, planet=planet, **satellite_data)

        actual = repr(satellite)
        expected = "<Satellite 'dummy_satellite'>"
        self.assertEqual(actual, expected)


if __name__ == "__main__":  # pragma: no cover
    main()


def run_tests():
    main()
