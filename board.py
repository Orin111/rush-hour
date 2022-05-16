#################################################################
# FILE : ex9.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION:this file ex9 board file
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
from car import Car


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.BOARD_SIZE = 7
        self.__graphic = self.create_board(self.BOARD_SIZE)
        self.__cars: dict[Car] = {}

    def get_graphic(self):
        return self.__graphic

    def create_board(self, BOARD_SIZE):
        board = []
        for row in range(BOARD_SIZE):
            row_list = []
            for col in range(BOARD_SIZE+1):
                if row == 3 and col == 7:
                    row_list.append('E')
                elif col < 7:
                    row_list.append('_')
            board.append(row_list)
        return board

    def get_cars(self):
        return self.__cars

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        str1 = ""
        for i in self.__graphic:
            str1 += "\n"
            str1 += str(i)
        return str1

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                lst.append((i, j))
        lst.append(self.target_location())
        return lst

    def in_board(self, c1):
        row, col = c1
        if row >= self.BOARD_SIZE or col >= self.BOARD_SIZE or row < 0 \
                or col < 0:
            return False
        return True

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        car_dict = self.__cars
        possible_moves = []
        for i in self.__cars.values():
            for direction in i.possible_moves():
                row, col = i.car_coordinates()[-1]
                if direction == 'd':
                    if not self.cell_content((row + 1, col)) and self.in_board((row + 1, col)):
                        possible_moves.append((i.get_name(), 'd', "car moves down"))
                elif direction == 'r':
                    if not self.cell_content((row, col + 1)) and self.in_board((row, col + 1)):
                        possible_moves.append((i.get_name(), 'r', "car moves right"))
                row, col = i.car_coordinates()[0]
                if direction == 'u':
                    if not self.cell_content((row - 1, col)) and self.in_board((row - 1, col)):
                        possible_moves.append((i.get_name(), 'u', "car moves up"))
                elif direction == 'l':
                    if not self.cell_content((row, col - 1)) and self.in_board((row, col - 1)):
                        possible_moves.append((i.get_name(), 'l', "car moves left"))
        return possible_moves

    def check_cars(self):
        lst = self.cell_list()
        for i in self.__cars.values():
            if i.car_coordinates() in lst:
                lst.remove(i.car_coordinates())
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        row = 3
        col = 7
        return (row, col)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars.values():
            if coordinate in car.car_coordinates():
                return car.get_name()

        return

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # check that the car name isn`t exist already
        for c in self.__cars:
            if c == car.get_name():
                return False
        # check that the car coordinates are on the board
        for i in car.car_coordinates():
            row, col = i
            if row >= self.BOARD_SIZE or col >= self.BOARD_SIZE or row < 0 \
                    or col < 0:
                return False
        # check that there is no car on those coordinates on the board
        for c in car.car_coordinates():
            row, col = c
            if self.__graphic[row][col] != "_":
                return False
        # add the car
        # add to the dict
        self.__cars[car.get_name()] = car
        # add to the graphic board
        for c in car.car_coordinates():
            row, col = c
            self.__graphic[row][col] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if not self.__cars.get(name):
            return False
        car1 = self.__cars[name]
        # check that the key is legal due to the car orientation
        if movekey not in car1.possible_moves():
            return False
        # check that the car coordinates are on the board
        # check that there is no car on those coordinates on the board
        row, col = car1.car_coordinates()[0]
        if movekey == 'u':
            if (row - 1, col) != self.target_location():
                if self.__graphic[row - 1][col] != "_" or (row-1, col) not in self.cell_list():
                    return False
        if movekey == 'l':
            if (row, col - 1) != self.target_location():
                if self.__graphic[row][col - 1] != "_" or (row, col-1) not in self.cell_list():
                    return False
        row, col = car1.car_coordinates()[-1]
        if movekey == 'r':
            if (row, col + 1) != self.target_location():
                if self.__graphic[row][col + 1] != "_" or (row, col+1) not in self.cell_list():
                    return False
        if movekey == 'd':
            if (row + 1, col) != self.target_location():
                if self.__graphic[row + 1][col] != "_" or (row+1, col) not in self.cell_list():
                    return False
        # clear the car`s location on the board
        for c in car1.car_coordinates():
            row, col = c
            self.__graphic[row][col] = "_"
        # update car`s new location
        car1.move(movekey)
        # update the dict
        self.__cars[car1] = car1
        # update the graphic board
        for c in car1.car_coordinates():
            row, col = c
            self.__graphic[row][col] = car1.get_name()
        return True

