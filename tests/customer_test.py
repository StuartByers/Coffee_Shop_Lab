import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("James", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("James", self.customer.name)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(2.50)
        self.assertEqual(97.50, self.customer.wallet)
