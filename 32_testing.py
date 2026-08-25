# ==========================
# UNIT TESTING
# ==========================

from hello import name_format
import unittest


class Test(unittest.TestCase):

    def test_1(self):

        content = name_format("rishat", "itvaya")

        self.assertEqual(content, {
            "first": "Rishat",
            "last": "Itvaya",
            "full": "Rishat Itvaya"
        })

    def test_2(self):

        content = name_format("rishat", "python")

        self.assertEqual(content, {
            "first": "Rishat",
            "last": "Python",
            "full": "Rishat Python"
        })


if __name__ == "__main__":
    unittest.main(verbosity=2)


# ==========================================================
# HOMEWORK
# ==========================================================

# 1. City, Country
#
# Create a function called city_country() that accepts
# a city and a country and returns them in this format:
#
# "Santiago, Chile"
#
# Put the function in a file called city_functions.py.
#
# Create another file called test_cities.py and use
# unittest to test the function.


# 2. City, Country with Population
#
# Modify city_country() so it can also accept a population.
#
# When a population is provided, return something like:
#
# "Santiago, Chile - population 5000000"
#
# Make population optional so the original function
# still works when no population is provided.
#
# Add another test to make sure the population version
# works correctly.