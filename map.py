# -*- coding: utf-8 -*-

from obstacle import *
from rectangle import *
import json

class Map:
    def __init__(self, entities = []):
        self.__entities = entities

    def getEntities(self):
        return self.__entities

    def setEntities(self, entities):
        self.entities = entities

    def addEntity(self, obstacle):
        self.__entities.append(obstacle)

    def removeEntity(self, obstacle):
        self.__entities.remove(obstacle)

    def removeEntityById(self, id):
        self.__entities.remove(obstacle)
        
    def serialize(self):
        entitiesSerialized = []
        for entity in self.__entities:
            entitiesSerialized.append(entity.serialize())
        s = {"class":"map", "entities":entitiesSerialized}
        return s

if __name__ == "__main__":
    pos = Position(7, 42, 69)
    rect = Rectangle(pos, 80, 60)
    something = []
    for i in range(10):
        rect.setWidth(i*10)
        o = Entity("e"+str(i), rect)
        something.append(o)
    map = Map(something)
    print(json.dumps(map.serialize()))
