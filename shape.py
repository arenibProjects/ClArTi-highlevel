# -*- coding: utf-8 -*-

import abc
from ../utils/position import *

class Shape(object, metaclass=abc.ABCMeta):
    _protectionRadius = 5 # default : in mm
    _position = Position()

    def isInside(self, position):
        raise NotImplementedError('users must define isInside to use this base class')

    def getProtectionRadius(self):
        return self._protectionRadius

    def setProtectionRadius(self, protectionRadius):
        if((protectionRadius > 0) and (protectionRadius < 1000)):
            self._protectionRadius = protectionRadius

    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position
        
    def serialize(self):
        s = {"class":"shape","position":self._position.serialize(),"protectionRadius":self._protectionRadius}
        return s
