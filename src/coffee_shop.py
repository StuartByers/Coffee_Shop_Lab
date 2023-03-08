class CoffeeShop:

    def __init__(self, name, till, Drinks): 
        self.name = name
        self.till = till
        self.drink = Drinks

    def increase_till(self, amount):
        self.till += amount

    