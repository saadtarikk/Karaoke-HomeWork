class Room:

    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.room_playlist = []
        self.occupants = []
        self.till = 0

    def can_pay(self, guest):
        if guest.wallet >= self.price:
            return True
        else:
            return False
    
    def till_accepts_money(self, guest, room):
        if self.can_pay(guest):
            room.till += room.price
            guest.wallet -= room.price


    def add_playlist_to_room(self, playlist):
        for song in playlist:
            self.room_playlist.append(song)
            # if song["track"] == guest.fav_song:
            #     return self.guest_cheer(guest)

    def add_single_guest_to_room(self, guest):
        if len(self.occupants) != self.capacity:
            if self.can_pay(guest):
                self.occupants.append(guest)
        else:
            return "Maximum Capacity reached"


    def add_guests_to_room(self, guests):
        if len(guests) <= self.capacity:
            for guest in guests:
                if self.can_pay(guest):
                    self.occupants.append(guest)
                else:
                    return "Alex doesn't have enough cash"
        else:
            return "Capacity reached"

    # def guest_has_fav_song_in_room(self, guest):
    #     for song in self.room_playlist:
    #         if song["track"] == guest.fav_song:
    #             return "whoo"

    def check_out_guests(self):
        self.occupants.clear()

            


    


    


           

