# Menu.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A simple class to define the shell around displayed menus

not initialised as will not be called on directly except through
initialised child classes.
"""


class Menu:
    _title = str
    _options = []

    def show_menu(self):
        print("-"*30)
        print("\t\t", self._title)
        print("-"*30)
        for i in self._options:
            print(i)

"""Test assertion:
If _title = "test menu"
And _options = ["1. test option 1", "2. test option 2", "3. test option 3"]
Then method should print string and list correctly
"""
"""
# test code:
my_menu_test = Menu()
my_menu_test._title = "test menu"
my_menu_test._options = ["1. test option 1", "2. test option 2", "3. test option 3"]
my_menu_test.show_menu()
#Test outcome: successful
"""