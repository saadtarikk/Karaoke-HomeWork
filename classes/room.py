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


    def guest_pays_for_entry(self, guest):
        guest.wallet -= self.price

    
    def till_accepts_money(self, room):
        room.till += room.price


    def add_playlist_to_room(self, playlist):
        for song in playlist:
            self.room_playlist.append(song)


    def add_single_guest_to_room(self, guest, room, playlist):
        if len(self.occupants) != self.capacity:
            if self.can_pay(guest):
                self.occupants.append(guest)
                self.guest_pays_for_entry(guest)
                self.till_accepts_money(room)
                self.add_playlist_to_room(playlist)
                self.guest_cheer(guest)
            else:
                return "You dont have enough cash"
        else:
            return "Maximum Capacity reached"


    def add_guests_to_room(self, guests, room, playlist):
        if len(guests) <= self.capacity:
            for guest in guests:
                if self.can_pay(guest):
                    self.occupants.append(guest)
                    self.guest_pays_for_entry(guest)
                    self.till_accepts_money(room)
                    self.add_playlist_to_room(playlist)
                    self.guest_cheer(guest)
            else:
                    return "Alex doesn't have enough cash"
        else:
            return "Capacity reached"


    def check_out_guests(self):
        self.occupants.clear()


    def check_out_single_guest(self, guest):
        self.occupants.remove(guest)


    def guest_cheer(self, guest):
        for song in self.room_playlist:
            if song.name == guest.fav_song:
                return "whoo"

            


    


    


           

