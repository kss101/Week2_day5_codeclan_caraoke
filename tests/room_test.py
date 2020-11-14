import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1", 2, 5)
        self.room2 = Room("Room 2", 3, 7.5)

        self.guest1 = Guest("Sam", 5)
        self.guest2 = Guest("Bob", 10)
        self.guest3 = Guest("Joe", 15)

        self.song1 = Song("People Like Us")

    def test_create_room( self ):
        self.assertEqual("Room 1", self.room1.name)

    def test_add_song_to_room( self ):
        self.room1.add_song( self.song1.name )
        self.assertEqual( 1, len(self.room1.song_list))

    def test_check_in_guest( self ):
        self.room1.check_in_guest( self.guest1.name )
        self.assertEqual( 1, len(self.room1.guest_list))

    def test_check_out_guest( self ):
        self.room1.check_in_guest( self.guest1.name )
        self.room1.check_in_guest( self.guest2.name )
        self.room1.check_out_guest( self.guest1.name )
        self.assertEqual( 1, len(self.room1.guest_list))
        self.assertEqual(['Bob'], self.room1.guest_list)

    def test_check_room_capacity( self ):
        self.assertEqual(2, self.room1.capacity)

    def test_room_capacity_exceeded( self ):
        self.room1.check_in_guest( self.guest1.name )
        self.room1.check_in_guest( self.guest2.name )
        self.assertEqual("Room full!", self.room1.check_in_guest(self.guest3.name))
        self.assertEqual(['Sam', 'Bob'], self.room1.guest_list)

    def test_charge_entry_fee( self ):
        self.room1.charge_entry_fee( self.guest1 )
        self.assertEqual(5, self.room1.cash_total )
        
