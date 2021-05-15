import unittest
from classes.bar import Bar
from classes.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        self.drink1 = Bar("Vodka", 4.00)
        self.drink2 = Bar("Beer", 3.00)
        self.drink3 = Bar("Rum", 4.00)

    def test_bar_has_drink(self):
        self.assertEqual("Vodka", self.drink1.name)

    def test_bar_has_drink_price(self):
        self.assertEqual(3.00, self.drink2.price)