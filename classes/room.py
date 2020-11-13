class Room:
    def __init__( self, name ):
        self.name = name
        self.song_list = []
        self.guest_list = []
    
    def add_song( self, song_name ):
        self.song_list.append(song_name)

    def check_in_guest( self, guest_name):
        self.guest_list.append(guest_name)

    def check_out_guest( self, guest_name ):
        for guest in self.guest_list:
            if guest == guest_name:
                self.guest_list.remove( guest )
