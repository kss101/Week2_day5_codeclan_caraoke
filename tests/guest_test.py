import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 10, "Eurovison Sing-Along")
        self.room1 = Room("Room 1", 2, 5)

    def test_create_guest( self ):
        self.assertEqual("Bob", self.guest.name)

    def test_get_favorite_song( self):
        self.assertEqual("Eurovison Sing-Along", self.guest.favourite_song)

    def test_can_pay_money( self ):
        self.assertEqual( True, self.guest.check_enough_money( 5 ))
    
    def test_cant_pay_money( self ):
        self.assertEqual( False, self.guest.check_enough_money( 15 ))
    
    def test_pay_money ( self ):
        self.guest.pay_money( 5 )
        self.assertEqual( 5, self.guest.money)

    def test_cheer_favorite_song ( self ):
      #  self.room1 = Room("Room 1", 2, 5)
        self.room1.add_song( "Waterloo" )
        self.room1.add_song( "Ice Cream" )
        self.room1.add_song( "Eurovison Sing-Along" )
        self.room1.add_song( "Nobody's Love" )
        self.assertEqual("WHOOOOHOOO!", self.guest.cheer_favourite_song( self.room1 ))

    def test_no_favorite_song_playing ( self ):
     #   self.room1 = Room("Room 1", 2, 5)
        self.room1.add_song( "Sucker" )
        self.room1.add_song( "Say Something" )
        self.room1.add_song( "Don't Be Sad" )
        self.room1.add_song( "Love You More" )
        self.assertEqual("Sad face :(", self.guest.cheer_favourite_song( self.room1 ))

