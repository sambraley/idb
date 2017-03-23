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

    def test_satellite_repr(self):
        example = Satellite("WGS-4 (USA-233)", "United Launch Alliance", \
                            "communications", 2012)
        actual = repr(example)
        expected = "Name: " + "WGS-4 (USA-233)" +             \
                    "\nAgency: " + "United Launch Alliance" + \
                    "\nType of Mission: " + "communications"+ \
                    "\nYear Launched: " + "2012"

        self.assertEqual(actual, expected)

    def test_satellite_assert(self):
        with self.assertRaises(AssertionError):
            Satellite("WGS-4 (USA-233)", "United Launch Alliance", \
                        "communications", 2012.0)

    def test_star_model(self):
        try:
            example = Star("HAT-P-33", "HAT-P-33.png",  6446.0, 1.0, \
                            113.184212, 33.835052, 1.38, None)

            with self.client.test_request_context():
                db.session.add(example)
                db.session.commit()

                star = db.session.query(Star).filter_by(name = "HAT-P-33").first()
                self.assertEqual(star.name, "HAT-P-33")
                self.assertEqual(star.mass, 1)

                db.session.delete(example)
                db.session.commit()
        except:
            db.session.rollback()
            raise

    def test_star_repr(self):
        example = Star("HAT-P-33", "HAT-P-33.png",  6446.0, 1.0, \
                        113.184212, 33.835052, 1.38, None)
        actual = repr(example)
        expected = "Name: " + "HAT-P-33" +                 \
                    "\nTemperature: " + "6446.0" +         \
                    "\nDiameter: " + "1.0" +               \
                    "\nRight Ascension: " + "113.184212" + \
                    "\nDeclination: " + "33.835052" +      \
                    "\nMass: " + "1.38" +                  \
                    "\nDistance: " + "None"

        self.assertEqual(actual, expected)

    def test_star_assert(self):
        with self.assertRaises(AssertionError):
            Star("HAT-P-33", "HAT-P-33.png",  6446.0, 1.0, 113, 33.835052, 1.38, None)

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

    def test_galaxy_repr(self):
        example = Galaxy("UGC 11693", "UGC 11693.png", \
                        317.819183, 37.884811, "spiral", 0.093554, 1.227)
        actual = repr(example)
        expected = "Name: " + "UGC 11693" +                \
                    "\nRight Ascension: " + "317.819183" + \
                    "\nDeclination: " + "37.884811" +      \
                    "\nGalaxy Type: " + "spiral" +         \
                    "\nRedshift: " + "0.093554" +          \
                    "\nAngular Size: " + "1.227"
        self.assertEqual(actual, expected)

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

    def test_planetoidBody_repr(self):
        example = PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018, \
                                984, 288.793037, 48.040234, 1.7841199999999998, \
                                0.0047126659923379345, 18.7959228)
        actual = repr(example)
        expected = "Name: " + "Kepler-117 b"+                 \
                    "\nDiameter: " + "100532.018"+            \
                    "\nSurface Temperature: " + "984" +       \
                    "\nRight Ascension: " + "288.793037"+     \
                    "\nDeclination: " + "48.040234"+          \
                    "\nMass: " + "1.7841199999999998" +       \
                    "\nGravity: " + "0.0047126659923379345" + \
                    "\nOrbital Period: " + "18.7959228"

        self.assertEqual(actual, expected)

    def test_planetoidBody_assert(self):
        with self.assertRaises(AssertionError):
            PlanetoidBody("Kepler-117 b", "Kepler-117 b.png", 100532.018, 984, 288.793037, \
                            48.040234, 1.7841199999999998, 0.0047126659923379345, 18)
if __name__ == "__main__":  # pragma: no cover
    main()
