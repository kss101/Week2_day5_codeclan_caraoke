class Guest:
    def __init__( self, name, money, favourite_song = '' ):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song

    def check_enough_money( self, amount ):
        if self.money >= amount:
            return True
        else:
            return False  

    def pay_money( self, amount ):
        check_money =  self.check_enough_money( amount )
        if check_money == True:
            self.money -= amount
            return True
        else:
            return False

    def cheer_favourite_song( self, room ):
        if self.favourite_song in room.song_list:
            return "WHOOOOHOOO!"
        else:
            return "Sad face :("
    