#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = pointless-string-statement


from unittest import main, TestCase

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

test_app = Flask(__name__)
test_app.config["SQLACLHEMY_DATABASE_URI"] = "sqlite:///:memory:"
test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from test_models import test_db, Satellite, Star, Galaxy, Planet

test_db.init_app(test_app)
with test_app.app_context():
    test_db.create_all()

star_data = {"name": "dummy_star", "temperature": 5945, "mass": 1.09, "diameter": 1405314.0,\
                "dec": -5.086445, "ra": 102.721137}

planet_data = {"name": "dummy_planet", "orbital_period": 1.327347, "temperature": 1823, \
                "mass": 3.477136e+27, "diameter": 176735.008, "gravity": 0.029718570060615346, \
                "dec": 44.915352, "ra": 188.266255}

satellite_data = {"name": "dummy_satellite", "mission_type": "Planetary Science", \
                    "info_url": "https://en.wikipedia.org/wiki/SARAL", "agency": \
                    "Indian Space Research Organization", "year_launched": 2013, \
                    "image": "https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"}

galaxy_data = {"name": "dummy_galaxy", "morph_type": "Spiral", "size": 1.227, "dec": 37.884811, \
                "ra": 317.819183, "redshift": 0.027192}

class TestModels (TestCase):

    def test_galaxy_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        galaxy = Galaxy(**galaxy_data)

        actual = galaxy.to_dict()

        for k, v in galaxy_data.items():
            self.assertEqual(actual[k], v)

    def test_galaxy_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        galaxy = Galaxy(**galaxy_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            actual = galaxy.to_dict()

            for k, v in galaxy_data.items():
                self.assertEqual(actual[k], v)

            test_db.session.delete(galaxy)
            test_db.session.commit()

            """
            Check to make sure row got deleted
            """
            galaxy =  test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)

    def test_galaxy_repr(self):
        """
        Checks model's correct representation is returned.
        """
        galaxy = Galaxy(**galaxy_data)

        actual = repr(galaxy)
        expected = "<Galaxy 'dummy_galaxy'>"
        self.assertEqual(actual, expected)


    def test_star_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)

        actual = star.to_dict()

        for k, v in star_data.items():
            self.assertEqual(actual[k], v)

    def test_star_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(name="dummy_star").first()
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
            star =  test_db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)

    def test_star_repr(self):
        """
        Checks model's correct representation is returned.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)

        actual = repr(star)
        expected = "<Star 'dummy_star'>"
        self.assertEqual(actual, expected)


    def test_planet_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)

        actual = planet.to_dict()

        for k, v in planet_data.items():
            self.assertEqual(actual[k], v)

    def test_planet_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(name="dummy_star").first()
            planet = test_db.session.query(Planet).filter_by(name="dummy_planet").first()

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
            star =  test_db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet =  test_db.session.query(Planet).filter_by(name="dummy_planet").first()
            self.assertEqual(planet, None)

    def test_planet_repr(self):
        """
        Checks model's correct representation is returned.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)

        actual = repr(planet)
        expected = "<Planet 'dummy_planet'>"
        self.assertEqual(actual, expected)

    def test_satellite_dictionary(self):
        """
        Examines model's to_dictionary() method for correctness in content.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)
        satellite = Satellite (galaxy = galaxy, star = star, planet = planet, **satellite_data)

        actual = satellite.to_dict()

        for k, v in satellite_data.items():
            self.assertEqual(actual[k], v)

    def test_satellite_model(self):
        """
        Adds row to database to make sure it gets added properly and removed properly.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)
        satellite = Satellite (galaxy = galaxy, star = star, planet = planet, **satellite_data)

        with test_app.test_request_context():
            test_db.session.add(galaxy)
            test_db.session.add(star)
            test_db.session.add(planet)
            test_db.session.add(satellite)
            test_db.session.commit()

            galaxy = test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = test_db.session.query(Star).filter_by(name="dummy_star").first()
            planet = test_db.session.query(Planet).filter_by(name="dummy_planet").first()
            satellite = test_db.session.query(Satellite).filter_by(name="dummy_satellite").first()

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
            star =  test_db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  test_db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet =  test_db.session.query(Planet).filter_by(name="dummy_planet").first()
            self.assertEqual(planet, None)
            satellite =  test_db.session.query(Satellite).filter_by(name="dummy_satellite").first()
            self.assertEqual(satellite, None)

    def test_satellite_repr(self):
        """
        Checks model's correct representation is returned.
        """
        galaxy = Galaxy(**galaxy_data)
        star = Star(galaxy = galaxy, **star_data)
        planet = Planet (galaxy = galaxy, star = star, **planet_data)
        satellite = Satellite (galaxy = galaxy, star = star, planet = planet, **satellite_data)

        actual = repr(satellite)
        expected = "<Satellite 'dummy_satellite'>"
        self.assertEqual(actual, expected)

if __name__ == "__main__":  # pragma: no cover
    main()

def run_tests():
    main()
