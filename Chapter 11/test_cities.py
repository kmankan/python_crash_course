import unittest
from city_functions import city_info


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """"Does it print a city and country?"""
        city_country = city_info('medellin', 'colombia')
        self.assertEqual(city_country,"Medellin, Colombia")

    def test_city_country_population(self):
        """Does it print city, country - population xxxx"""
        city_country_population = city_info('santiago', 'chile',
                                            population=500000)
        self.assertEqual(city_country_population,
                         "Santiago, Chile - Population 500000")


if __name__ == '__main__':
    unittest.main
