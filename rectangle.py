# -*- coding: utf-8 -*-

from shape import *

class Rectangle(Shape):
    
    def __init__(self, position, w, h):
        self._position = position
        self.__width = w
        self.__height = h

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height
    
    def isInside(self, position):
        # 1 - Se ramener à une AABB (Axis-Aligned Bounding Box)
        theta = position.getHeading()

        # - Translation
        offsetX = position.getX() - self._position.getX()
        offsetY = position.getY() - self._position.getY()

        # - Rotation (inverse)
        testX = math.cos(-theta) * offsetX + math.cos(-theta) * offsetY
        testY = math.sin(-theta) * offsetX + math.cos(-theta) * offsetY

        # 2 - Simplifier le test (symétries)
        testX = math.fabs(testX)
        testY = math.fabs(testY)

        # 3 - Tests
        if((testX > (self.__width + self.__protectionRadius) / 2) or (testY > (self.__height + self.__protectionRadius) / 2)): # Si on est en dehors de la AABB globale (avec le radius)
            return False
        else: # On est dedans
            # Coin du rectangle
            refX = self.__width / 2
            refY = self.__height / 2
            
            if(((testX - refX) < 0) or ((testY - refY) < 0)): # Si on est pas dans le coin de protection (zone où la détection se fait comme un cercle)
                return True
            elif(math.sqrt((testX - refX)**2 + (testY - refX)**2) < self.__protectionRadius): # Si, dans le coin, on est dans le rayon de protection
                return True
            else:
                return False

    def serialize(self):
        s = Shape.serialize(self)
        s["class"] = "rectangle"
        s["width"] = self.__width
        s["height"] = self.__height
        return s
        
if __name__ == "__main__":
    pos = Position(7, 42, 69)
    rect = Rectangle(pos, 80, 60)
    print(json.dumps(rect.serialize()))
