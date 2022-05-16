#################################################################
# FILE : ex9.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION:this file ex9 car file
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
class Car:
    """
    Add class description here
    """
    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def get_length(self):
        return self.__length

    def get_orientation(self):
        return self.__orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        car_coordinates = []
        row = self.__location[0]
        col = self.__location[1]
        for i in range(self.__length):
            if self.__orientation == 1:
                car_coordinates.append((row, col + i))
            elif self.__orientation == 0:
                car_coordinates.append((row + i, col))
        return car_coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        if self.__orientation == 0:
            return {'u': "car moves up", 'd': "car moves down"}
        elif self.__orientation == 1:
            return {'r': "car moves right", 'l': "car moves left"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        car_coordinates = self.car_coordinates()
        row, col = self.car_coordinates()[-1]
        if movekey == 'r':
            return [(row, col + 1)]
        if movekey == 'd':
            return [(row + 1, col)]
        row, col = self.car_coordinates()[0]
        if movekey == 'u':
            return [(row - 1, col)]
        if movekey == 'l':
            return [(row, col - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        row, col = self.car_coordinates()[0]
        if self.__orientation == 0:
            if movekey == 'u':
                self.__location = (row - 1, col)
                return True
            if movekey == 'd':
                self.__location = (row + 1, col)
                return True
            return False
        if self.__orientation == 1:
            if movekey == 'r':
                self.__location = (row, col + 1)
                return True
            if movekey == 'l':
                self.__location = (row, col - 1)
                return True
            return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.__name
