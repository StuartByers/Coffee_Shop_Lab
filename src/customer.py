class Customer:

    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def increase_energy_level(self, drink):
        self.energy_level += drink.caffeine_level
        

    def buy_drink(self, drink, coffee_shop):
        if self.wallet >= drink.price:
           self.wallet -= drink.price
           coffee_shop.till += drink.price
           self.increase_energy_level(drink)

    # test for customer buying drink
    #  call wallet decrease
    #  call till increase
    #  call energy increase




        # if wallet >= drink price
        # reduce wallet by drink price
        # add to drink price to till



        # drink needs to come from drink.name
        # price needs to come from drink.price
