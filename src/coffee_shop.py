class CoffeeShop:

    def __init__(self, name, till, Drinks): 
        self.name = name
        self.till = till
        self.drink = Drinks

    def increase_till(self, amount):
        self.till += amount
    
    def check_age(self, customer):
        print(customer.__dict__)
        if customer.age >= 16:
            return True
        else:
            return False

    