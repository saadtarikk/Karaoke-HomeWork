class Guest:

    def __init__(self, name, age, wallet, fav_song):
        self.name = name
        self.age = age 
        self.wallet = float(wallet)
        self.fav_song = fav_song
        
    def sufficient_funds(self, drink):
        return self.wallet >= drink.price

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price