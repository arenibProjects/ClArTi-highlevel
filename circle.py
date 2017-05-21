# -*- coding: utf-8 -*-

import math
from shape import *

class Circle(Shape):
    def __init__(self, position, r):
        self._position = position
        self.__radius = r
    
    def isInside(self, position):
        distance = math.sqrt((position.getX() - self._position.getX())**2 + (position.getY() - self._position.getY())**2)

        if(distance > self.__radius + self._protectionRadius):
            return False
        else:
            return True

    def serialize(self):
        s = Shape.serialize(self)
        s["class"] = "circle"
        s["radius"] = self.__radius
        return s

if __name__ == "__main__":
    pos = Position(7, 42, 69)
    circle = Circle(pos, 6)
    print(json.dumps(circle.serialize()))
