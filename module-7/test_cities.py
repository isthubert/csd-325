# Isaac St Hubert Module 7.2 11/22/2025
# This program tests the city_country function using unittest

from city_functions import city_country

import unittest

class Test_format(unittest.TestCase):

    def test_city_country(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()
