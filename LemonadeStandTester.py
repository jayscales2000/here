# Author: Jalen Scales
# GitHub username: jalenscales
# Date: 09/26/2024
# Description: Write code to keep track of lemonade stand menu items and daily sales. Three classes are to be created,
# MenuItem, SaleForDay, LemonadeStand.

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class TestLemonadeStand(unittest.TestCase):

    def test_menu_item(self):
        """test for menu item"""
        item = MenuItem('lemonade', 0.75, 1.5)
        self.assertEqual(item.get_name(), 'lemonade')
        self.assertEqual(item.get_wholesale_price(), 0.75)
        self.assertEqual(item.get_selling_price(), 1.5)

    def test_sales_for_day(self):
        """test for day sales"""
        sales_dict = {'lemonade': 5, 'cookie': 4}
        sales = SalesForDay(1, sales_dict)
        self.assertEqual(sales.get_day(), 1)
        self.assertEqual(sales.get_sales_dict(), sales_dict)

    def test_lemonade_stand(self):
        """tests lemonade stand object"""
        stand = LemonadeStand('Test Stand')
        item = MenuItem('lemonade', 0.75, 1.5)
        stand.add_menu_item(item)
        self.assertEqual(stand.get_name(), 'Test Stand')
        self.assertEqual(stand.total_sales_for_menu_item('lemonade'), 0)

    def test_sales_for_today_correct(self):
        """tests for correct sales items"""
        stand = LemonadeStand('Test Stand')
        item = MenuItem('lemonade', 0.75, 1.5)
        stand.add_menu_item(item)
        stand.enter_sales_for_today({'lemonade': 20})
        self.assertEqual(stand.total_sales_for_menu_item('lemonade'), 20)

    def test_sales_for_today_incorrect(self):
        """test for incorrect sales items"""
        stand = LemonadeStand('Test Stand')
        item = MenuItem('lemonade', 0.75, 1.5)
        stand.add_menu_item(item)
        with self.assertRaises(InvalidSalesItemError):
            stand.enter_sales_for_today({'pepsi': 5})

if __name__ == '__main__':
    unittest.main()
