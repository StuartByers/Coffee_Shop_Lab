class Customer:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, Drink):
        if self.wallet >= self.Drink.price:
           self.wallet.remove(self.Drink.price)
           self.CoffeeShop.increase(self.Drink.price)
        #    self.CoffeeShop.till.append(self.Drink.price)


        # if wallet >= drink price
        # reduce wallet by drink price
        # add to drink price to till



        # drink needs to come from drink.name
        # price needs to come from drink.price
