# PlacementInstructions.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class InfoString defining this specific block string

Initialises the block string applying information to be printed to screen
when called
"""

from InfoString import InfoString


class PlacementInstructions(InfoString):

    def __init__(self):
        self._text = """------------------------------------
\t\tPlacement Instructions
------------------------------------

You have two ships, each is 3 squares long. To place them first chose
the starting point for each then chose the oreientation of your ship
either vertical or horizontal. Your ship will be placed from there e.g.
coordernates 1,1 and orentation of horizontal your ship would be placed
at coordernates 1,1 , 1,2 , 1,3:

\t\t|   _____________   |
\t\t|  | 1 S S S ~ ~ |  |
\t\t|  | 2 ~ ~ ~ ~ ~ |  |
\t\t|  | 3 ~ ~ ~ ~ ~ |  |
\t\t|  | 4 ~ ~ ~ ~ ~ |  |
\t\t|  | 5 ~ ~ ~ ~ ~ |  |
\t\t|  |   1 2 3 4 5 |  |
\t\t|  |_____________|  |
"""

"""Test assertion:
If instance created
Then use parent class show_text()
Then method should print string
"""
"""
#test code:
my_string_test = PlacementInstructions()
my_string_test.show_text()
#tested successfully
"""