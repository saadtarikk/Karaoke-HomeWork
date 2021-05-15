import unittest
from classes.song import Song
from classes.room import Room
class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Queen", "Bohemian Rhapsody")

        self.song1 = Song("Linken park", "In the end")
        self.song2 = Song("Natasha Bedingfield", "Unwritten")
        self.song4 = Song("Linken park", "In the end")

        self.playlist =[self.song, self.song1, self.song2]

        

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song.artist)

    def test_song_has_name(self):
        self.assertEqual("Bohemian Rhapsody", self.song.name)

    def test_song_has_playlist(self):
        self.assertEqual(3, len(self.playlist))