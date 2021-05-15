import unittest
from classes.song import Song
from classes.room import Room
class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = {
            "artist": "Queen",
            "track": "Bohemian Rhapsody"
        }

        self.song1 = {
            "artist": "Linken park",
            "track": "In the end"
        }
        self.song2 = {
            "artist": "Natasha Bedingfield",
            "track": "Unwritten"
        }

        self.playlist = [{
            "artist": "Queen",
            "track": "Bohemian Rhapsody",
        },
        {
            "artist": "Linken park",
            "track": "In the end"
        },
        {
            "artist": "Natasha Bedingfield",
            "track": "Unwritten"
        }]

        

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song["artist"])

    def test_song_has_name(self):
        self.assertEqual("Bohemian Rhapsody", self.song["track"])

    def test_song_has_playlist(self):
        self.assertEqual(3, len(self.playlist))