# WelcomeMessage.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class InfoString defining this specific block string

Initialises the block string applying information to be printed to screen
when called
"""

from InfoString import InfoString


class WelcomeMessage(InfoString):

    def __init__(self):
        self._text = """Welcome to battleships. In this console game you play against the computer
taking turns to shot at guessed target locations until you sink your opponents
fleet or they sink yours.
"""


"""Test assertion:
If instance created
Then use parent class show_text()
Then method should print string
"""
"""
#test code:
my_string_test = WelcomeMessage()
my_string_test.show_text()
#tested successfully
"""