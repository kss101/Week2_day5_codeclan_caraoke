import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob")

    def test_create_guest( self ):
        self.assertEqual("Bob", self.guest.name)