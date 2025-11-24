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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
