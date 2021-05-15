import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Boiler room", 20, 5)
        self.room2 = Room("Grinder room", 35, 3)
        self.guest = Guest("Jack", 28, 50.00, "In the end")
        self.guest1 = Guest("Andy", 35, 75.00, "In the end")
        self.guest2 = Guest("Alex", 25, 30.00, "Unwritten")
        self.guest3 = Guest("Collin", 30, 45.00, "Dancing in the moonlight")
        self.guests1 = [self.guest, self.guest1, self.guest2]
        self.guests2 = [self.guest, self.guest1, self.guest2, self.guest3]
        self.guests3 = [self.guest1, self.guest2, self.guest3]
        self.song = Song("Queen", "Bohemian Rhapsody")

        self.song1 = Song("Linken park", "In the end")
        self.song2 = Song("Natasha Bedingfield", "Unwritten")
        self.song4 = Song("Linken park", "In the end")
        self.playlist = [self.song, self.song1, self.song2]

        #make a list with 2 guest with enough money and one with not enough and test it

        #take money off customer wallet and add it to till for room price
        # self.playlist = [{
        #     "artist": "Queen",
        #     "track": "Bohemian Rhapsody",
        # },
        # {
        #     "artist": "Linken park",
        #     "track": "In the end"
        # },
        # {
        #     "artist": "Natasha Bedingfield",
        #     "track": "Unwritten"
        # }]



    def test_room_has_name(self):
        self.assertEqual("Boiler room", self.room1.name)

    def test_room_has_price(self):
        self.assertEqual(20, self.room1.price)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room2.capacity)

    def test_room_has_playlist(self):
        self.assertEqual(3, len(self.playlist))
    
    def test_guest_can_pay_for_room(self):
        self.assertEqual(True, self.room1.can_pay(self.guest))

    def test_customer_pays_for_room(self):
        self.room1.guest_pays_for_entry(self.guest1)
        self.assertEqual(55, self.guest1.wallet)

    def test_till_accepts_money(self):
        self.room1.till_accepts_money(self.room1)
        self.assertEqual(20, self.room1.till)
    

    def test_can_add_playlist_to_room(self):
        self.room1.add_playlist_to_room(self.playlist)
        self.assertEqual(3, len(self.room1.room_playlist))

    def test_add_single_guest_to_room(self):
        self.room1.add_single_guest_to_room(self.guest, self.room1, self.playlist)
        self.assertEqual(1, len(self.room1.occupants))
        self.assertEqual(20, self.room1.till)
        self.assertEqual(30, self.guest.wallet)
        self.assertEqual(3, len(self.room1.room_playlist))
        self.assertEqual("whoo", self.room1.room_playlist)

    
    def test_can_add_guests_to_room_true(self):
        self.room2.add_guests_to_room(self.guests1, self.room2)
        self.assertEqual(2, len(self.room2.occupants))
        self.assertEqual(70, self.room2.till)
        self.assertEqual(15, self.guest.wallet)
        self.assertEqual(40, self.guest1.wallet)
        

    def test_can_add_guest_room_false(self):
        self.assertEqual("Capacity reached", self.room2.add_guests_to_room(self.guests2, self.room2))

    def test_cant_pay_for_room(self):
        self.assertEqual("Alex doesn't have enough cash", self.room2.add_guests_to_room(self.guests3, self.room2))

    # def test_guest_has_fav_song_in_room_playlist(self):
    #     self.assertEqual("whoo", self.room1.guest_has_fav_song_in_room(self.guest1))

    def test_can_checkout_guest(self):
        self.room1.check_out_guests()
        self.assertEqual(0, len(self.room1.occupants))

    def test_can_check_out_single_guest(self):
        self.room2.add_single_guest_to_room(self.guest, self.room2, self.playlist)
        self.room2.check_out_single_guest(self.guest)
        self.assertEqual(0, len(self.room1.occupants))

   

