# Sea.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19

"""the main class that generates the three game boards used to construct the game"""


class Sea:
    _top = """ ____________________
|  Targeting Board   |"""
    _middle = """|____________________|
|____________________|
|     Your Board     |"""
    _bottom = "|____________________|\n"

    def __init__(self):
        """To generate a unique game board from the template"""
        self.board = [["|   ______________   |"],
                      ["|  | 1", "~", "~", "~", "~", "~", " |  |"],
                      ["|  | 2", "~", "~", "~", "~", "~", " |  |"],
                      ["|  | 3", "~", "~", "~", "~", "~", " |  |"],
                      ["|  | 4", "~", "~", "~", "~", "~", " |  |"],
                      ["|  | 5", "~", "~", "~", "~", "~", " |  |"],
                      ["|  |  ", "1", "2", "3", "4", "5", " |  |"],
                      ["|  |______________|  |"]
                      ]

    def show_sea_board(self):
        """To display the current game board."""
        for i in self.board:
            print(*i)

    def get_is_position_valid(self, x, y, orientation):
        """To check if a specified position is valid."""
        is_valid = False
        try:
            if orientation == "h" and self.board[x][y] == "~" and self.board[x][y + 1] == "~" and self.board[x][y + 2] == "~":
                is_valid = True
                return is_valid
            elif orientation == "v" and self.board[x][y] == "~" and self.board[x + 1][y] == "~" and self.board[x + 2][y] == "~":
                is_valid = True
                return is_valid
            else:
                return is_valid
        except IndexError:
            return is_valid
        except ValueError:
            return is_valid

    def update_position(self, x, y, orientation):
        """To be run only if position has been validated."""
        if orientation == "h":
            self.board[x][y] = "S"
            self.board[x][y + 1] = "S"
            self.board[x][y + 2] = "S"
        elif orientation == "v":
            self.board[x][y] = "S"
            self.board[x + 1][y] = "S"
            self.board[x + 2][y] = "S"

    def get_guess_is_valid(self, x, y):
        """To check if a specified position is valid."""
        is_valid = False
        try:
            if self.board[x][y] == "~":
                is_valid = True
                return is_valid
            elif self.board[x][y] == "S":
                is_valid = True
                return is_valid
            else:
                return is_valid
        except IndexError:
            return is_valid
        except ValueError:
            return is_valid

    def update_result(self, x, y):
        """To be run only if position has been validated."""
        result = ""
        if self.board[x][y] == "S":
            self.board[x][y] = "X"
            result = "Hit"
            return result
        else:
            self.board[x][y] = "M"
            result = "Miss"
            return result

"""Test assertion 1: testing show_sea_board()
If instance created
Then method should print to screen correctly
"""
"""
# test code 1:
my_player_board_test = Sea()
my_player_board_test.show_sea_board()
# test outcome 1: successful
"""

"""Test assertion 2: testing show_sea_board()
If instance created for 2*board
and additional print statments to factor in the boarder
Then method should print string
"""
"""
# test code 2:
my_player_board_test = Sea()
my_guess_board_test = Sea()
print(my_player_board_test._top)
my_guess_board_test.show_sea_board()
print(my_player_board_test._middle)
my_player_board_test.show_sea_board()
print(my_player_board_test._bottom)
#Test outcome 2: successful
"""

"""Test assertion 3: testing get_is_position_valid()
if instance created
then additional parameters:
x = 1
y = 1
orientation = h
then method should validate
"""
"""
# test code 3:
my_test_board = Sea()
x = 1
y = 1
orientation = "h"
validate_is = (my_test_board.get_is_position_valid(x,y,orientation))
print(validate_is)
# test outcome 3: successful
"""

"""Test assertion 4: testing get_is_position_valid() if invalid
if instance created
then additional parameters:
x = 1
y = 9
orientation = h
then method should invalidate
"""
"""
# test code 4:
my_test_board = Sea()
x = 1
y = 9
orientation = "h"
validate_is = (my_test_board.get_is_position_valid(x,y,orientation))
print(validate_is)
# test outcome 4: successful
"""

"""Test assertion 5: testing update_position()
if instance created
then additional parameters:
x = 1
y = 1
orientation = h
then method should update the instance
then display the updated instance instance
"""
"""
# test code 5:
my_test_board = Sea()
x = 1
y = 1
orientation = "h"
if my_test_board.get_is_position_valid(x, y, orientation) == True:
    my_test_board.update_position(x, y, orientation)
    my_test_board.show_sea_board()
else:
    print("You can't place a ship there, please try again.")
    my_test_board.show_sea_board()
# test outcome 5: successful
"""

"""Test assertion 6: testing update_position() if invalid
if instance created
then additional parameters:
x = 1
y = 1
orientation = h
then method should update the instance
then display the updated instance instance
then new parameters:
x = 1
y = 1
orientation = v
then repeated using these new peramitors that over lap the already filled postion
then displays invlaid postion message
then displays instance with no update
"""
"""
# test code 6:
my_test_board = Sea()
x = 1
y = 1
orientation = "h"
if my_test_board.get_is_position_valid(x, y, orientation) == True:
    my_test_board.update_position(x, y, orientation)
    my_test_board.show_sea_board()
else:
    print("You can't place a ship there, please try again.")
    my_test_board.show_sea_board()
x = 1
y = 1
orientation = "v"
if my_test_board.get_is_position_valid(x, y, orientation) == True:
    my_test_board.update_position(x, y, orientation)
    my_test_board.show_sea_board()
else:
    print("You can't place a ship there, please try again.")
    my_test_board.show_sea_board()
# test outcome 6: successful
"""

"""Test assertion 7: testing get_guess_is_valid()
if instance created
then additional parameters:
x = 1
y = 1
then should return valid
"""
"""
#test code 7:
my_test_board = Sea()
x = 1
y = 1
validate_is = (my_test_board.get_guess_is_valid(x,y))
print(validate_is)
# test outcome 7: successful
"""

"""Test assertion 8: testing get_guess_is_valid() if invalid
if instance created
then additional parameters:
x = 1
y = 9
then should return valid
"""
"""
#test code 8:
my_test_board = Sea()
x = 1
y = 9
validate_is = (my_test_board.get_guess_is_valid(x,y))
print(validate_is)
# test outcome 8: successful
"""

"""Test assertion 9: testing update_result()
if instance created
then instace displayed
then peramitors created:
x = 3
y = 3
then method should update instance correctly
then intance displayed to confirm
"""
"""
# test code 9:
my_test_board = Sea()
print("without update")
my_test_board.show_sea_board()
x = 3
y = 3
my_test_board.update_result(x, y)
print("with update")
my_test_board.show_sea_board()
# test outcome 9: successful
"""