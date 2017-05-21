# -*- coding: utf-8 -*-

import math

class Position:
    def __init__(self, x = 0, y = 0, heading = 0):
        self.__x = x
        self.__y = y
        self.__heading = heading
    
    def getX(self):
        return self.__x
    
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__y
    
    def setY(self, y):
        self.__y = y
    
    def getHeading(self):
        return self.__heading
    
    def setHeading(self, heading):
        self.__heading = self.normalizeAngle(heading)

    def normalizeAngle(self, angle):
        while(angle < - math.pi):
            angle += 2*math.pi
        while(angle > math.pi):
            angle -= 2*math.pi
        return angle

    def serialize(self):
        return {"class":"position","x":self.__x, "y":self.__y, "heading":self.__heading}

if __name__ == "__main__":
    pos = Position(7, 42, 69)
    print(json.dumps(pos.serialize()))
