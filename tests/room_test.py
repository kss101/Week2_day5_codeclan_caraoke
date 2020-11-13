import unittest
from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")
        self.room2 = Room("Room 2")

    def test_create_room( self ):
        self.assertEqual("Room 1", self.room1.name)

    def test_check_in_guest( self ):
        guest = Guest("Sam")
        self.room1.check_in_guest( guest.name )
        self.assertEqual( 1, len(self.room1.guest_list))

    def test_check_out_guest( self ):
        guest1 = Guest("Sam")
        guest2 = Guest("Bob")
        self.room1.check_in_guest( guest1.name )
        self.room1.check_in_guest( guest2.name )
        self.room1.check_out_guest( guest1.name )
        self.assertEqual( 1, len(self.room1.guest_list))
        self.assertEqual(['Bob'], self.room1.guest_list)
    
       
