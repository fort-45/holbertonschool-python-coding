#!/usr/bin/python3
'''
doc of module
'''


class Square:
    '''
    another documentation for the class
    '''
    def __init__(self, size=0):
        '''
        this method will check if the
        size type is integer and if
        it is greater or equal than o
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Retrieves the private instance attribute __size
        (The Gettet)
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the private instance attribute __size
        (The Setter)
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        this returns the area of square
        '''
        return self.__size ** 2
