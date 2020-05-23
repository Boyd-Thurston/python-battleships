# TitleText.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""A child class to parent class InfoString defining this specific block string

Initialises the block string applying information to be printed to screen
when called
"""

from InfoString import InfoString


class TitleText(InfoString):

    def __init__(self):
        self._text = """
 _____       __    _______   _______   _      _____    ___    _    _   _   ____     ___      __
|  _  \     /  \  |__   __| |__   __| | |    |  ___|  / _ \  | |  | | | | |  _ \   / _ \    |  |
| |_|  |   / /\ \    | |       | |    | |    | |__   | | |_| | |__| | | | | |_| | | | |_|   |  |
|    _/   / /__\ \   | |       | |    | |    |  __|   \ \    |  __  | | | |  __/   \ \      |  |
|  _  \  |  ____  |  | |       | |    | |    | |      _ \ \  | |  | | | | | |      _ \ \    |__|
| |_|  | | |   |  |  | |       | |    | |__  | |___  | |_| | | |  | | | | | |     | |_| |    __
|_____/  |_|   |__|  |_|       |_|    |____| |_____| \_____/ |_|  |_| |_| |_|     \_____/   |__|

"""

"""Test assertion:
If instance created
Then use parent class show_text()
Then method should print string
"""
"""
#test code:
my_string_test = TitleText()
my_string_test.show_text()
#tested successfully
"""