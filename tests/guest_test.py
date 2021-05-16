import unittest
from classes.guest import Guest
from classes.bar import Bar

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("jack", 28, 50.00, "Dancing Queen")
        self.guest2 = Guest("andy", 35, 75.00, "In the end")
        self.drink1 = Bar("Vodka", 4.00)
        self.drink2 = Bar("Beer", 3.00)
        self.drink3 = Bar("Rum", 6.00)


    def test_guest_has_name(self):
        self.assertEqual("jack", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(28, self.guest.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Dancing Queen", self.guest.fav_song)

    def test_guest_has_sufficient_funds_for_drink(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.drink1))

    def test_guest_can_buy_drink(self):
        self.guest.buy_drink(self.drink3)
        self.assertEqual(44.00, self.guest.wallet)
   