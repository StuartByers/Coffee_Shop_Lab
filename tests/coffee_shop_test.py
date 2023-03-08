import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("Starbucks", 300.00, "Espresso")
        self.customer = Customer("David", 45.00, 21, 1)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name)

    def test_can_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(302.50, self.coffee_shop.till)

    def test_check_age(self):
        self.assertEqual(True, self.coffee_shop.check_age(self.customer))