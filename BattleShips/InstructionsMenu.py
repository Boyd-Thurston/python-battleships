# InstructionsMenu.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class Menu defining this specific menu

Initialises the InstructionsMenu applying information to be printed to screen
when accessing this menu and methods of use when options are selected.
"""

from Menu import Menu
from PlacementInstructions import PlacementInstructions
from GameInstructions import GameInstructions


class InstructionsMenu(Menu):

    def __init__(self):
        self._title = "Instructions Menu"
        self._options = ["1. Placement Instructions", "2. Game Instructions", "3. Back"]

    def select_menu_option(self):
        counter_1 = 0
        while counter_1 == 0:
            try:
                command = int(input("\nWhat would you like to do?\n"))
                if command == 1:
                    # shows placement instructions
                    i = PlacementInstructions()
                    i.show_text()
                    self.show_menu()
                elif command == 2:
                    # shows game play instruction
                    i = GameInstructions()
                    i.show_text()
                    self.show_menu()
                elif command == 3:
                    # exits the menu
                    counter_1 += 1
                else:
                    print("That is not a valid response.")
            except ValueError:
                print("That is not a valid response.")

"""Test assertion:
If instance created
Then parent class show_menu() function is called
Then method should print string and list correctly
"""

"""
"# test code:
my_menu_test = TitleMenu()
my_menu_test.show_menu()
#Test outcome: successful
"""


"""Test assertion 1: testing display
If instance created
Then parent class show_menu() function is called
Then method should print string and list correctly
"""
"""Test assertion 2: testing PlacementInstructions()
If instance created
Then parent class show_menu() function is called
Then input = 1
Then method should print Placement Instructions
"""
"""Test assertion 3: testing GameInstructions()
If instance created
Then parent class show_menu() function is called
Then input = 2
Then method should print Game Instructions
"""
"""Test assertion 4: testing exit
If instance created
Then parent class show_menu() function is called
Then input = 3
Then method should end Instructions Menu instance
"""
"""
# test code:
my_menu_test = InstructionsMenu()
my_menu_test.show_menu()
#Test outcome 1: successful
my_menu_test.select_menu_option()
#Test outcome 2: successful
#Test outcome 3: successful
#Test outcome 4: successful
"""