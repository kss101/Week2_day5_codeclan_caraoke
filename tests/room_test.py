import unittest
from classes.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")

    def test_create_room( self ):
        self.assertEqual("Room 1", self.room1.name)