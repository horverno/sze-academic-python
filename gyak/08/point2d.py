#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Siki Zoltán
class Point2D(object): # object a bázis osztály
    """ kettő dimenziós pontok osztálya
    """
    def __init__(self, east = 0, north = 0): # __init__ a konstruktor
        """ Initialize point
        :param east: első koordináta
        :param north: második koordináta
        """
        self.east = east # tagváltozó létrehozása
        self.north = north
    def abs(self):
        """ calculate length of vector (absolute value)
        :returns: absolute value
        """
        return (self.east**2 + self.north**2)**0.5