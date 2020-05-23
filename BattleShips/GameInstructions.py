# GameInstructions.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class InfoString defining this specific block string

Initialises the block string applying information to be printed to screen
when called
"""

from InfoString import InfoString


class GameInstructions(InfoString):

    def __init__(self):
        self._text = """-------------------------------
\t\tGame Institutions
-------------------------------

To play: shoot a missle at a coordinate on the gameboard. Try
to hit the two enemy ships of length 3.

you do this by first entering the row you wish to targert down the side:

\t\t| 1 ~
\t\t| 2 ~
\t\t| 3 ~
\t\t| 4 ~
\t\t| 5 ~

then by entering the column you wish to target along the bottom:

\t\t| 5 ~ ~ ~ ~ ~ |
\t\t|   1 2 3 4 5 |
\t\t|_____________|

The computer will then do the same.

You and the computer both take turns to shoot, and be the first one to
get 6 hits on the enemies board WINS!
"""

"""Test assertion:
If instance created
Then use parent class show_text()
Then method should print string
"""
"""
#test code:
my_string_test = GameInstructions()
my_string_test.show_text()
#tested successfully
"""
