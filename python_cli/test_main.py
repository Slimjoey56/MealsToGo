import unittest

from main import MENU, Restaurant, money


class RestaurantTests(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Test Kitchen", MENU)

    def test_add_item_and_calculate_subtotal(self):
        self.assertTrue(self.restaurant.add_to_cart("1", 2))
        self.assertAlmostEqual(self.restaurant.subtotal(), 90.00)
        self.assertEqual(self.restaurant.item_count(), 2)

    def test_invalid_item_is_not_added(self):
        self.assertFalse(self.restaurant.add_to_cart("99"))
        self.assertEqual(self.restaurant.cart, {})

    def test_zero_quantity_is_rejected(self):
        self.assertFalse(self.restaurant.add_to_cart("1", 0))

    def test_remove_item(self):
        self.restaurant.add_to_cart("2")
        self.assertTrue(self.restaurant.remove_from_cart("2"))
        self.assertFalse(self.restaurant.remove_from_cart("2"))
        self.assertEqual(self.restaurant.subtotal(), 0)

    def test_clear_cart(self):
        self.restaurant.add_to_cart("3", 2)
        self.restaurant.clear_cart()
        self.assertEqual(self.restaurant.cart, {})
        self.assertEqual(self.restaurant.item_count(), 0)

    def test_money_format(self):
        self.assertEqual(money(12), "GH₵12.00")


if __name__ == "__main__":
    unittest.main()
