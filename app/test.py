#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from unittest import main, TestCase
from idb import app, db
from models import Satellite, Star, Galaxy, Planet


star_data = {"name": "dummy_star", "temperature": 5945, "mass": 1.09, "diameter": 1405314.0,\
                "dec": -5.086445, "ra": 102.721137}

planet_data = {"name": "dummy_planet", "orbital_period": 1.327347, "temperature": 1823, \
                "mass": 3.477136e+27, "diameter": 176735.008, "gravity": 0.029718570060615346, \
                "dec": 44.915352, "ra": 188.266255}

satellite_data = {"name": "dummy_satellite", "mission_type": "Planetary Science", \
                    "info_url": "https://en.wikipedia.org/wiki/SARAL", "agency": "Indian Space Research Organization", \
                    "year_launched": 2013, "image": "https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"}

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

        with app.test_request_context():
            db.session.add(galaxy)
            db.session.commit()

            galaxy = db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            actual = galaxy.to_dict()

            for k, v in galaxy_data.items():
                self.assertEqual(actual[k], v)

            db.session.delete(galaxy)
            db.session.commit()

            """
            Check to make sure row got deleted
            """
            galaxy =  db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
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

        with app.test_request_context():
            db.session.add(galaxy)
            db.session.add(star)
            db.session.commit()

            galaxy = db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = db.session.query(Star).filter_by(name="dummy_star").first()
            actual = star.to_dict()

            for k, v in star_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(star.galaxy_pid, galaxy.pid)

            db.session.delete(star)
            db.session.delete(galaxy)
            db.session.commit()

            """
            Check to make sure row got deleted
            """
            star =  db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
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

        with app.test_request_context():
            db.session.add(galaxy)
            db.session.add(star)
            db.session.commit()

            galaxy = db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = db.session.query(Star).filter_by(name="dummy_star").first()
            planet = db.session.query(Planet).filter_by(name="dummy_planet").first()

            actual = planet.to_dict()

            for k, v in planet_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(planet.star_pid, star.pid)
            self.assertEqual(planet.galaxy_pid, galaxy.pid)


            db.session.delete(star)
            db.session.delete(galaxy)
            db.session.delete(planet)
            db.session.commit()

            """
            Check to make sure row got deleted
            """
            star =  db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet =  db.session.query(Planet).filter_by(name="dummy_planet").first()
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

        with app.test_request_context():
            db.session.add(galaxy)
            db.session.add(star)
            db.session.add(planet)
            db.session.add(satellite)
            db.session.commit()

            galaxy = db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            star = db.session.query(Star).filter_by(name="dummy_star").first()
            planet = db.session.query(Planet).filter_by(name="dummy_planet").first()
            satellite = db.session.query(Satellite).filter_by(name="dummy_satellite").first()

            actual = satellite.to_dict()

            for k, v in satellite_data.items():
                self.assertEqual(actual[k], v)

            """
            Make sure that correct that foreign keys were mapped correctly.
            """
            self.assertEqual(satellite.galaxy_pid, galaxy.pid)
            self.assertEqual(satellite.star_pid, star.pid)
            self.assertEqual(satellite.planet_pid, planet.pid)


            db.session.delete(star)
            db.session.delete(galaxy)
            db.session.delete(planet)
            db.session.delete(satellite)
            db.session.commit()

            """
            Check to make sure row got deleted
            """
            star =  db.session.query(Star).filter_by(name="dummy_star").first()
            self.assertEqual(star, None)
            galaxy =  db.session.query(Galaxy).filter_by(name="dummy_galaxy").first()
            self.assertEqual(galaxy, None)
            planet =  db.session.query(Planet).filter_by(name="dummy_planet").first()
            self.assertEqual(planet, None)
            satellite =  db.session.query(Satellite).filter_by(name="dummy_satellite").first()
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

    # def test_galaxy_assert(self):
    #     """
    #     Makes sure precoditions are checked and assertion thrown.
    #     """
    #     with self.assertRaises(AssertionError):
    #         Galaxy("UGC 11693", "UGC 11693.png",
    #                317.819183, 37.884811, 0, 0.093554, 1.227)

    # def tearDown(self):
    #     """
    #     Removes current Session associated wih test case.
    #     """
    #     db.session.remove()

    # def test_satellite_model(self):
    #     """
    #     Adds row to database to make sure it gets added properly.
    #     """
    #     example = Satellite(**satellite_data, satar=Star()galaxy=Galaxy(**galaxy_data))

    #     with app.test_request_context():
    #         db.session.add(example)
    #         db.session.commit()

    #         satellite = db.session.query(Satellite).filter_by(name="dummy_satellite").first()
            
    #         self.assertEqual(satellite.name, "dummy_satellite")
    #         self.assertEqual(satellite.year_launched, 2013)

    #         db.session.delete(example)
    #         db.session.commit()

    # def test_satellite_dictionary(self):
    #     """
    #     Examines model's dictionary() method for correctness in content.
    #     """
    #     example = Satellite("WGS-4 (USA-233)", "United Launch Alliance",
    #                         "communications", 2012)
    #     actual = example.dictionary()

    #     self.assertEqual(actual["name"], "WGS-4 (USA-233)")
    #     self.assertEqual(actual["agency"], "United Launch Alliance")
    #     self.assertEqual(actual["mission"], "communications")
    #     self.assertEqual(actual["year_launched"], 2012)

    # def test_satellite_assert(self):
    #     """
    #     Makes sure precoditions are checked and assertion thrown.
    #     """
    #     with self.assertRaises(AssertionError):
    #         Satellite("WGS-4 (USA-233)", "United Launch Alliance",
    #                   "communications", 2012.0)

    # def test_star_model(self):
    #     """
    #     Adds row to database to make sure it gets added properly.
    #     """
    #     try:
    #         example = Star("HAT-P-33", "HAT-P-33.png", 6446.0,
    #                        113.184212, 33.835052, 1.38)

    #         with app.test_request_context():
    #             db.session.add(example)
    #             db.session.commit()

    #             star = db.session.query(Star).filter_by(
    #                 name="HAT-P-33").first()
    #             self.assertEqual(star.name, "HAT-P-33")
    #             self.assertEqual(star.mass, 1.38)

    #             db.session.delete(example)
    #             db.session.commit()
    #     except:
    #         db.session.rollback()
    #         raise

    # def test_star_dictionary(self):
    #     """
    #     Examines model's dictionary() method for correctness in content.
    #     """
    #     example = Star("HAT-P-33", "HAT-P-33.png",  6446.0,
    #                    113.184212, 33.835052, 1.38)
    #     actual = example.dictionary()

    #     self.assertEqual(actual["name"], "HAT-P-33")
    #     self.assertEqual(actual["image"], "HAT-P-33.png")
    #     self.assertEqual(actual["temperature"], 6446.0)
    #     self.assertEqual(actual["right_ascension"], 113.184212)
    #     self.assertEqual(actual["declination"], 33.835052)
    #     self.assertEqual(actual["mass"], 1.38)
    #     self.assertEqual(actual["planetoid_bodies"], ())
    #     self.assertEqual(actual["satellites"], ())

    # def test_star_assert(self):
    #     """
    #     Makes sure precoditions are checked and assertion thrown.
    #     """
    #     with self.assertRaises(AssertionError):
    #         Star("HAT-P-33", "HAT-P-33.png",  6446.0, 113, 33.835052, 1.38)

    # def test_planetoidBody_model(self):
    #     """
    #     Adds row to database to make sure it gets added properly.
    #     """
    #     try:
    #         example = PlanetoidBody(
    #             "Kepler-117 b", "Kepler-117 b.png", 100532.018,
    #             84.0, 288.793037, 48.040234, 1.7841199999999998,
    #             0.0047126659923379345, 18.7959228)

    #         with app.test_request_context():
    #             db.session.add(example)
    #             db.session.commit()

    #             planetoidBody = db.session.query(PlanetoidBody).filter_by(
    #                 name="Kepler-117 b").first()
    #             self.assertEqual(planetoidBody.name, "Kepler-117 b")
    #             self.assertEqual(planetoidBody.gravity, 0.0047126659923379345)

    #             db.session.delete(example)
    #             db.session.commit()
    #     except:
    #         db.session.rollback()
    #         raise

    # def test_planetoidBody_dictionary(self):
    #     """
    #     Examines model's dictionary() method for correctness in content.
    #     """
    #     example = PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018,
    #                             984.0, 288.793037, 48.040234, 1.7841199999999998,
    #                             0.0047126659923379345, 18.7959228)
    #     actual = example.dictionary()

    #     self.assertEqual(actual["name"], "Kepler-117 b")
    #     self.assertEqual(actual["image"], "Kepler-117 b.png")
    #     self.assertEqual(actual["diameter"], 100532.018)
    #     self.assertEqual(actual["temperature"], 984.0)
    #     self.assertEqual(actual["right_ascension"], 288.793037)
    #     self.assertEqual(actual["declination"], 48.040234)
    #     self.assertEqual(actual["mass"], 1.7841199999999998)
    #     self.assertEqual(actual["gravity"], 0.0047126659923379345)
    #     self.assertEqual(actual["orbital_period"], 18.7959228)
    #     self.assertEqual(actual["orbiting_bodies"], None)
    #     self.assertEqual(actual["satellites"], None)

    # def test_planetoidBody_assert(self):
    #     """
    #     Makes sure precoditions are checked and assertion thrown.
    #     """
    #     with self.assertRaises(AssertionError):
    #         PlanetoidBody(
    #             "Kepler-117 b", "Kepler-117 b.png", 100532.018, 984, 288.793037,
    #             48.040234, 1.7841199999999998, 0.0047126659923379345, 18)
if __name__ == "__main__":  # pragma: no cover
    main()
