# -*- coding: utf-8 -*-

from shape import *

class Obstacle:
    def __init__(self, shape):
        self.__shape = shape

    def getShape(self):
        return self.__shape

    def setShape(self, shape):
        self.__shape = shape

    def serialize(self):
        s = {"class":"obstacle", "shape":self.__shape.serialize()}
        return s
