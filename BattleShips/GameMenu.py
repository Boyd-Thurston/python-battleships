# GameMenu.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class Menu defining this specific menu

Initialises the GameMenu applying information to be printed to screen
when accessing this menu and methods of use when options are selected.
"""

from Menu import Menu
from GameInstructions import GameInstructions


class GameMenu(Menu):

    def __init__(self):
        self._title = "Game Menu"
        self._options = ["1. Continue", "2. Game Instructions"]

    def select_menu_option(self):
        counter_1 = 0
        while counter_1 == 0:
            try:
                command = int(input("\nWhat would you like to do?\n"))
                if command == 1:
                    # exits the menu
                    counter_1 += 1
                elif command == 2:
                    # shows game play instruction
                    i = GameInstructions()
                    i.show_text()
                    self.show_menu()
                else:
                    print("That is not a valid response.")
            except ValueError:
                print("That is not a valid response.")

"""Test assertion 1: testing display
If instance created
Then parent class show_menu() function is called
Then method should print string and list correctly
"""
"""Test assertion 2: testing GameInstructions()
If instance created
Then parent class show_menu() function is called
Then input = 2
Then method should print Game Instructions and re display menu
"""
"""Test assertion 3: testing exit
If instance created
Then parent class show_menu() function is called
Then input = 1
Then method should end Game Menu instance
"""
"""
# test code:
my_menu_test = GameMenu()
my_menu_test.show_menu()
my_menu_test.select_menu_option()
#Test outcome 1: successful
#Test outcome 2: successful
#Test outcome 3: successful
"""