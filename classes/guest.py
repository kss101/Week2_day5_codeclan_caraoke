class Guest:
    def __init__( self, name, money ):
        self.name = name
        self.money = money

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
    