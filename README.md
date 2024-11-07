[70 pts] You will be writing code for recording the menu items and daily sales of a lemonade stand. It will have these classes: MenuItem, SalesForDay, and LemonadeStand. All data members of each class should be marked as private (a leading underscore in the name). Since they're private, if you need to access them from outside the class, you should do so via get or set methods.

Here are descriptions of the three classes:

MenuItem:

A MenuItem object represents a menu item to be offered for sale at the lemonade stand. It has three data members:

a string for the item's name
a float for the item's wholesale cost (how much the stand pays for the item)
a float for the item's selling price (how much the stand sells the item for)
The Menu Item methods are:

init method - takes three parameters (name, wholesale cost, selling price) and uses them to initialize the data members
get methods for each of the data members: get_name(), get_wholesale_cost(), and get_selling_price()
SalesForDay:

A SalesForDay object represents the sales for a particular day. It has two data members:

an integer for the number of days the stand has been open so far
a dictionary whose keys are the names of the items sold and whose values are the numbers of those items sold that day
The SalesForDay methods are:

init method - takes two parameters (number of days, sales dictionary) and uses them to initialize the data members
get methods for each of the data members: get_day() and get_sales_dict()
LemonadeStand: Remember that the LemonadeStand class must not directly access the private data members of MenuItem and SalesForDay objects, but instead must call the appropriate get methods

A LemonadeStand object represents a lemonade stand. It has four data members:

a string for the name of the stand
an integer representing the current day
a dictionary of MenuItem objects, where the keys are the names of the items and the values are the corresponding MenuItem objects
a list of SalesForDay objects
The LemonadeStand methods are:

