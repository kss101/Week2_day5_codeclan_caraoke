class Room:
    def __init__( self, name, capacity, entry_fee ):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.song_list = []
        self.guest_list = []
        self.cash_total = 0
    
    def add_song( self, song_name ):
        self.song_list.append(song_name)

    def check_in_guest( self, guest_name):
        if self.capacity > 0:
            self.guest_list.append(guest_name)
            self.capacity -= 1
        else:
            return "Room full!"

    def check_out_guest( self, guest_name ):
        for guest in self.guest_list:
            if guest == guest_name:
                self.guest_list.remove( guest )

    def charge_entry_fee( self, guest ):
        guest_payed = guest.pay_money( self.entry_fee )
        if guest_payed == True:
            self.cash_total += self.entry_fee


