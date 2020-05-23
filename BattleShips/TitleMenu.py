# TitleMenu.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class Menu defining this specific menu

Initialises the GameMenu applying information to be printed to screen
when accessing this menu and methods of use when options are selected.
"""

from Menu import Menu


class TitleMenu(Menu):

    def __init__(self):
        self._title = "Title Menu"
        self._options = ["1. Start a new game", "2. Instructions", "3. Exit Battleships"]

    def start_game(self):
        print("New game starting")


"""Test assertion:
If instance created
Then parent class show_menu() function is called
Then method should print string and list correctly
"""
"""
# test code:
my_menu_test = TitleMenu()
my_menu_test.show_menu()
#Test outcome: successful
"""