# TitleBanner.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class InfoString defining this specific block string

Initialises the block string applying information to be printed to screen
when called
"""

from InfoString import InfoString


class TitleBanner(InfoString):

    def __init__(self):
        self._text = """
|                  _                                 \/\/                              _                   |
|                 | |                                <{}>                             | |                  |
|                 | |  _                       O     /\/\   O                      _  | |                  |
|                 | | | \                                                         / | | |                  |
|              _  | | |  \                                                       /  | | |  _               |
|             / | | | |   \             O                          O            /   | | | | \              |
|            /  | | | |    \                                                   /    | | | |  \             |
|           /   | | | |     \                                                 /     | | | |   \            |
|          /    | | | |      \       __                             __       /      | | | |    \           |
|         /     | | | |       \     / /                             \ \     /       | | | |     \          |
|        /______| | | |________\  _/ /                               \ \_  /________| | | |______\         |
|       __________| |____________(_)/___                           ___\(_)____________| |__________        |
|       \                              /                           \                              /        |
|        \                            /                             \                            /         |
|         \__________________________/                               \__________________________/          |
"""

"""Test assertion:
If instance created
Then use parent class show_text()
Then method should print string
"""
"""
#test code:
my_string_test = TitleBanner()
my_string_test.show_text()
#tested successfully
"""
