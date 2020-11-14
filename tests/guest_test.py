import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 10)

    def test_create_guest( self ):
        self.assertEqual("Bob", self.guest.name)

    def test_can_pay_money( self ):
        self.assertEqual( True, self.guest.check_enough_money( 5 ))
    
    def test_cant_pay_money( self ):
        self.assertEqual( False, self.guest.check_enough_money( 15 ))
    
    def test_pay_money ( self ):
        self.guest.pay_money( 5 )
        self.assertEqual( 5, self.guest.money)


