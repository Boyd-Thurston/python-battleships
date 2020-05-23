# MainProgram.py
#
# author Karan Soma, Boyd Thurston
# date: 28.11.19


import random

from Sea import Sea
from PlacementInstructions import PlacementInstructions
from TitleBanner import TitleBanner
from TitleMenu import TitleMenu
from InstructionsMenu import InstructionsMenu
from GameMenu import GameMenu
from TitleText import TitleText
from WelcomeMessage import WelcomeMessage


def show_title_page():
    # displays title splash page
    banner = TitleBanner()
    title = TitleText()
    message = WelcomeMessage()
    banner.show_text()
    title.show_text()
    message.show_text()
    input("press enter to continue")


def player_placement(player_board):
    # placement instructions
    instructions = PlacementInstructions()
    instructions.show_text()

    # player placement
    placed = 0
    while placed < 2:
        try:
            x = int(input("Chose a row?\n"))
            y = int(input("Chose a column?\n"))
            orientation = input("For orientation enter h for horizontal or v for vertical?\n")
            if player_board.get_is_position_valid(x, y, orientation) == True:
                player_board.update_position(x, y, orientation)
                placed += 1
                player_board.show_sea_board()
            else:
                print("You can't place a ship there, please try again.")
                player_board.show_sea_board()
        except ValueError:
            print("That is not a valid entry, please try again.")
    return player_board


def computer_placement(computer_board):
    # generating computers placement
    placed = 0
    while placed < 2:
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        orientation_options = ("h", "v")
        orientation = random.choice(orientation_options)
        if computer_board.get_is_position_valid(x, y, orientation) == True:
            computer_board.update_position(x, y, orientation)
            placed += 1
    return computer_board


def new_game():
    # creating variables
    player_board = Sea()
    computer_board = Sea()
    guess_board = Sea()
    user_hits = 0
    computer_hits = 0
    # placing ships
    player_placement(player_board)
    computer_placement(computer_board)
    print("Good you are ready. Now lets begin.\n")
    input("press enter to start")
    # starting rounds
    while user_hits < 6 and computer_hits < 6:
        # players turn
        while user_hits < 6:
            print(player_board._top)
            guess_board.show_sea_board()
            print(player_board._middle)
            player_board.show_sea_board()
            print(player_board._bottom)
            try:
                y_guess = int(input("please enter the row to target or enter 0 to see in game menu\n"))
                while y_guess == 0:
                    i = GameMenu()
                    i.show_menu()
                    i.select_menu_option()
                    y_guess = int(input("please enter the row to target or enter 0 to see in game menu\n"))
                x_guess = int(input("please enter the column to target or enter 0 to see in game menu\n"))
                while x_guess == 0:
                    i = GameMenu()
                    i.show_menu()
                    i.select_menu_option()
                    x_guess = int(input("please enter the column to target or enter 0 to see in game menu\n"))
                if computer_board.get_guess_is_valid(y_guess, x_guess) == True:
                    result = computer_board.update_result(y_guess, x_guess)
                    print("Your shot was a {0}".format(result))
                    if result == "Hit":
                        user_hits += 1
                        guess_board.board[y_guess][x_guess] = "X"
                    else:
                        guess_board.board[y_guess][x_guess] = "M"
                    break
                else:
                    print("that is not a valid location. try again\n")
            except ValueError:
                print("That is not a valid entry, please try again.")
        if user_hits == 6:
            print("You Won!")
            computer_hits = 7
        # computers turn
        while computer_hits < 6:
            x_guess_2 = random.randint(1, 5)
            y_guess_2 = random.randint(1, 5)
            print("\nThe computer shot at {0},{1}".format(x_guess_2, y_guess_2))
            if player_board.get_guess_is_valid(y_guess_2, x_guess_2) == True:
                result = player_board.update_result(y_guess_2, x_guess_2)
                print("It's shot was a {0}".format(result))
                if result == "Hit":
                    computer_hits += 1
                break
        if computer_hits == 6:
            print("You Lost!")


# main program
# Display title splash page
show_title_page()
# Displaying the Title Menu
main_menu = TitleMenu()
main_menu.show_menu()
counter_1 = 0
while counter_1 == 0:
    try:
        command = int(input("\nWhat would you like to do?\n"))
        if command == 1:
            # starts a new game
            main_menu.start_game()
            new_game()
            main_menu.show_menu()
        elif command == 2:
            # shows instruction menu
            i = InstructionsMenu()
            i.show_menu()
            i.select_menu_option()
            main_menu.show_menu()
        elif command == 3:
            # exits the program
            counter_1 += 1
            # program exit
            print("Good Bye!")
            input("press enter to exit.")
        else:
            print("That is not a valid response.")
    except ValueError:
        print("That is not a valid response.")
