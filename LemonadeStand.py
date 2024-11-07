# Author: Jalen Scales
# GitHub username: jalenscales
# Date: 09/26/2024
# Description: Write code to keep track of lemonade stand menu items and daily sales. Three classes are to be created,
# MenuItem, SaleForDay, LemonadeStand.

class MenuItem:
    """creates menu object with three attributes, item name, wholesale price, selling price."""

    def __init__(self, name, wholesale_price, selling_price):
        self._name = name
        self._wholesale_price = wholesale_price
        self._selling_price = selling_price

    def get_name(self):
        """gets menu item name"""
        return self._name

    def get_wholesale_price(self):
        """gets wholesale price"""
        return self._wholesale_price

    def get_selling_price(self):
        """gets selling price"""
        return self._selling_price


class SalesForDay:
    """represents sales for a particular day"""

    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """gets day"""
        return self._day

    def get_sales_dict(self):
        """creates sales dictionary """
        return self._sales_dict


class InvalidSalesItemError(Exception):
    pass


class LemonadeStand:
    """creates a lemonade stand object"""

    def __init__(self, stand_name):
        self._stand_name = stand_name
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """gets stand name"""
        return self._stand_name

    def add_menu_item(self, menu_item):
        """gets menu item"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """gets sales for day"""
        for item in sales_dict:
            if item not in self._menu:
                raise InvalidSalesItemError(f"Invalid sales item: {item}")
        sales_for_day = SalesForDay(self._current_day, sales_dict)
        self._sales_record.append(sales_for_day)
        self._current_day += 1

    def get_sales_dict_for_day(self, day):
        """gets dictionary for day"""
        for sold in self._sales_record:
            if sold.get_day() == day:
                return sold.get_sales_dict()
        return {}

    def total_sales_for_menu_item(self, item_name):
        """gets total sales for menu item"""
        total_sold = 0
        for sales in self._sales_record:
            sales_dict = sales.get_sales_dict()
            total_sold += sales_dict.get(item_name, 0)
        return total_sold

    def total_profit_for_menu_item(self, item_name):
        """gets total profit for menu item"""
        total_sold = self.total_sales_for_menu_item(item_name)
        if item_name not in self._menu:
            return 0
        menu_item = self._menu[item_name]
        profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_price()
        return total_sold * profit_per_item

    def total_profit_for_stand(self):
        """gets total profit from stand"""
        profit = 0
        for item_name in self._menu:
            profit += self.total_profit_for_menu_item(item_name)
        return profit

