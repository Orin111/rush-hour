#################################################################
# FILE : ex9.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION:this file ex9 game file
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import sys

import helper
import helper as h
from board import Board
from car import Car


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board

    def __single_turn(self):
        """

        :return: True if game continue
        False if game ended
        """
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        # check if the game has ended -on start
        print(self.board)
        target_r, target_c = self.board.target_location()
        if self.board.get_graphic()[target_r][target_c] != "E":
            print("you won")
            return False
        if not self.board.possible_moves():
            return False
        # get input
        user_input = input(
            "enter the car color, direction (enter ! to finish the game)")
        # check if the player asked to end the game
        if user_input == "!":
            return False
        color, d = user_input.split(",")
        # check the the direction is legal
        if d not in ['u', 'd', 'l', 'r']:
            print("please enter a legal direction: 'u', 'd', 'l', 'r' ")
            return True
        # check that the car name is legal
        if color not in self.board.get_cars():
            print("please enter a legal color")
            return True
        # try to move the car
        if not self.board.move_car(color, d):
            print("move is illegal")
        else:
            print(self.board)
            # check if the game has ended
            target_r, target_c = self.board.target_location()
            if self.board.get_graphic()[target_r][target_c] != "E":
                print("you won")
                return False
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while game.__single_turn():
            continue
        return


def create_board(json_file):
    car_config = h.load_json(json_file)
    board1 = Board()
    for c in car_config:
        name = c
        length = car_config[c][0]
        row, col = car_config[c][1][0], car_config[c][1][1]
        location = (row, col)
        orientation = car_config[c][2]
        # check that the car length is legal
        if length > 4 or length < 2:
            continue
        # check that the car orientation is legal
        if orientation not in [0, 1]:
            continue
        # check that the car name is legal
        if name not in ['R', 'G', 'W', 'O', 'B', 'Y']:
            continue
        # create the car
        car1 = Car(name, length, location, orientation)
        # check that the car on the board and add the car
        board1.add_car(car1)
    return board1


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    s = sys.argv
    url = s[1]
    game = Game(create_board(url))
    game.play()
