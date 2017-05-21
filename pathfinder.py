# -*- coding: utf-8 -*-

import abc
from trajectory import *

class Pathfinder(object, metaclass=abc.ABCMeta):
    _path = Trajectory()
    
    def __init__(self, m = None):
        self._map = m

    def getMap(self):
        return self._map

    def setMap(self, m):
        self._map = m

    def getPath(self):
        return self._path

    def findPath(self):
        raise NotImplementedError('users must define findPath to use this base class')

