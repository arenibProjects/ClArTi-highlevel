# -*- coding: utf-8 -*-

from position import *

class Trajectory:
    def __init__(self, positions = []):
        self.__positions = positions

    def setPositions(self):
        return self.__positions

    def getPositions(self, positions):
        self.__positions = positions

    def addPosition(self, position):
        self.__positions.append(position)

    def removePosition(self, position):
        self.__positions.remove(position)

    def getStart(self):
        return self.__positions[0]

    def getGoal(self):
        return self.__positions[-1]

    def serialize(self):
        positionsSerialized = []
        for position in self.__positions:
            positionsSerialized.append(position.serialize())
        
        s = {"class":"trajectory", "positions":positionsSerialized}
        return s
