# -*- coding: utf-8 -*-

class Entity:
    def __init__(self, id, shape):
        self.__id = id
        self.__shape = shape

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getShape(self):
        return self.__shape

    def setShape(self, shape):
        self.__shape = shape
        
    def serialize(self):
        s = {"class":"entity", "id":id, "shape":Shape.serialize(self.__shape)}
        return s
