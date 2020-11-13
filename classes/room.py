class Room:
    def __init__( self, name ):
        self.name = name
        self.song_list = []
        self.guest_list = []
    
    def check_in_guest( self, guest_name):
        self.guest_list.append(guest_name)