import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("People Like Us")

    def test_song_exists( self ):
        self.assertEqual("People Like Us", self.song1.name)
