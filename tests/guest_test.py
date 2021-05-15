import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("jack", 28, 50.00, "Dancing Queen")
        self.guest2 = Guest("andy", 35, 75.00, "In the end")


    def test_guest_has_name(self):
        self.assertEqual("jack", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(28, self.guest.age)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Dancing Queen", self.guest.fav_song)

    def guest_cheer(self):
        return "whoo"
    #- Create rooms, songs and guests
# - Check in guests to rooms/Check out guests from rooms
# - Add songs to rooms