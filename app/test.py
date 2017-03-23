#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from unittest import main, TestCase
from models import db, Satellite, Star, Galaxy, PlanetoidBody
from idb import app

class TestModels (TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()

    def test_satellite_model(self):
        try:
            example = Satellite("WGS-4 (USA-233)", "United Launch Alliance", \
                                "communications", 2012)

            with self.client.test_request_context():
                db.session.add(example)
                db.session.commit()

                satellite = db.session.query(Satellite).filter_by(name = "WGS-4 (USA-233)").first()
                self.assertEqual(satellite.name, "WGS-4 (USA-233)")
                self.assertEqual(satellite.year_launched, 2012)

                db.session.delete(example)
                db.session.commit()
        except:
            db.session.rollback()
            raise

    def test_satellite_dictionary(self):
        example = Satellite("WGS-4 (USA-233)", "United Launch Alliance", \
                            "communications", 2012)
        actual = example.dictionary()

        self.assertEqual(actual["name"], "WGS-4 (USA-233)")
        self.assertEqual(actual["agency"], "United Launch Alliance")
        self.assertEqual(actual["type_of_mission"], "communications")
        self.assertEqual(actual["year_launched"], 2012)


    def test_satellite_assert(self):
        with self.assertRaises(AssertionError):
            Satellite("WGS-4 (USA-233)", "United Launch Alliance", \
                        "communications", 2012.0)

    def test_star_model(self):
        try:
            example = Star("HAT-P-33", "HAT-P-33.png", 6446.0,  \
                            113.184212, 33.835052, 1.38)

            with self.client.test_request_context():
                db.session.add(example)
                db.session.commit()

                star = db.session.query(Star).filter_by(name = "HAT-P-33").first()
                self.assertEqual(star.name, "HAT-P-33")
                self.assertEqual(star.mass, 1.38)

                db.session.delete(example)
                db.session.commit()
        except:
            db.session.rollback()
            raise

    def test_star_dictionary(self):
        example = Star("HAT-P-33", "HAT-P-33.png",  6446.0, \
                        113.184212, 33.835052, 1.38)
        actual = example.dictionary()

        self.assertEqual(actual["name"], "HAT-P-33")
        self.assertEqual(actual["image"], "HAT-P-33.png")
        self.assertEqual(actual["temperature"], 6446.0)
        self.assertEqual(actual["righ_ascension"], 113.184212)
        self.assertEqual(actual["declination"], 33.835052)
        self.assertEqual(actual["mass"], 1.38)
        self.assertEqual(actual["planetoid_bodies"], None)
        self.assertEqual(actual["satellites"], None)

    def test_star_assert(self):
        with self.assertRaises(AssertionError):
            Star("HAT-P-33", "HAT-P-33.png",  6446.0, 113, 33.835052, 1.38)

    def test_galaxy_model(self):
        try:
            example = Galaxy("UGC 11693", "UGC 11693.png", \
                            317.819183, 37.884811, "spiral", 0.093554, 1.227)

            with self.client.test_request_context():
                db.session.add(example)
                db.session.commit()

                galaxy = db.session.query(Galaxy).filter_by(name = "UGC 11693").first()
                self.assertEqual(galaxy.name, "UGC 11693")
                self.assertEqual(galaxy.size, 1.227)

                db.session.delete(example)
                db.session.commit()
        except:
            db.session.rollback()
            raise

    def test_galaxy_dictionary(self):
        example = Galaxy("UGC 11693", "UGC 11693.png", \
                        317.819183, 37.884811, "spiral", 0.093554, 1.227)
        actual = example.dictionary()

        self.assertEqual(actual["name"], "UGC 11693")
        self.assertEqual(actual["image"], "UGC 11693.png")
        self.assertEqual(actual["righ_ascension"], 317.819183)
        self.assertEqual(actual["declination"], 37.884811)
        self.assertEqual(actual["galaxy_type"], "spiral")
        self.assertEqual(actual["redshift"], 0.093554)
        self.assertEqual(actual["angular_size"], 0.093554)
        self.assertEqual(actual["stars"], None)
        self.assertEqual(actual["planetoid_bodies"], None)
        self.assertEqual(actual["satellites"], None)

    def test_galaxy_assert(self):
        with self.assertRaises(AssertionError):
            Galaxy("UGC 11693", "UGC 11693.png", \
                    317.819183, 37.884811, 0, 0.093554, 1.227)

    def test_planetoidBody_model(self):
        try:
            example = PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018, \
                                    984, 288.793037, 48.040234, 1.7841199999999998, \
                                    0.0047126659923379345, 18.7959228)

            with self.client.test_request_context():
                db.session.add(example)
                db.session.commit()

                planetoidBody = db.session.query(PlanetoidBody).filter_by(name = \
                                                            "Kepler-117 b").first()
                self.assertEqual(planetoidBody.name, "Kepler-117 b")
                self.assertEqual(planetoidBody.gravity, 0.0047126659923379345)

                db.session.delete(example)
                db.session.commit()
        except:
            db.session.rollback()
            raise

    def test_planetoidBody_dictionary(self):
        example = PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018, \
                                984, 288.793037, 48.040234, 1.7841199999999998, \
                                0.0047126659923379345, 18.7959228)
        actual = example.dictionary()

        self.assertEqual(actual["name"], "Kepler-117 b")
        self.assertEqual(actual["image"], "Kepler-117 b.png")
        self.assertEqual(actual["diameter"], 100532.018)
        self.assertEqual(actual["temperature"], 984)
        self.assertEqual(actual["righ_ascension"], 288.793037)
        self.assertEqual(actual["declination"], 48.040234)
        self.assertEqual(actual["mass"], 1.7841199999999998)
        self.assertEqual(actual["gravity"], 0.0047126659923379345)
        self.assertEqual(actual["orbital_period"], 18.7959228)
        self.assertEqual(actual["orbiting_bodies"], None)
        self.assertEqual(actual["satellites"], None)

    def test_planetoidBody_assert(self):
        with self.assertRaises(AssertionError):
            PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018, 984, 288.793037, \
                            48.040234, 1.7841199999999998, 0.0047126659923379345, 18)
if __name__ == "__main__":  # pragma: no cover
    main()
