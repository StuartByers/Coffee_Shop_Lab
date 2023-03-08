import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Latte", 2.50)

    def test_drink_has_name(self):
        self.assertEqual("Latte", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(2.50, self.drink.price)