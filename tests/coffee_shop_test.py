import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("Starbucks", 300.00, "Espresso")
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Starbucks", self.coffee_shop.name)

    def test_can_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(302.50, self.coffee_shop.till)