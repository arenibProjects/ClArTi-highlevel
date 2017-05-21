# -*- coding: utf-8 -*-

##    A* algorithm implementation, based on pseudo-code from https://en.wikipedia.org/wiki/A%2a_search_algorithm.
##    Created 07/05/2017 for Eurobot 2017
##    /!\ Every position in mm /!\

import math

from pathfinder import *
from ../utils/trajectory import *

class Astar(Pathfinder):
    __w = 3000
    __h = 2000
    
    def __init__(self, m = None):
        Pathfinder.__init__(self, m)

        # Working Grid
        self.__workingGrid = [[0 for x in range(self.__w)] for y in range(self.__h)]

    # update the grid used to check the neighborhood of each node (= avoid obstacles)
    def updateWorkingGrid(self):
        for y in range(self.__h):
            for x in range(self.__w):
                
                # Entities in map
                for shape in self._others.getShape():
                    if(shape.isInside(Position(x, y, 0))):
                        self.__baseGrid[y][x] = 1
                    else:
                        self.__baseGrid[y][x] = 0

    def findPath(self, startPos, goalPos):
        # Before A*
        self.updateWorkingGrid()

        # A*
        goal = {"position":goalPos, "f":math.inf, "g":math.inf, "comeFrom":None}
        start = {"position":startPos, "f":-1, "g":0, "comeFrom":None}
        start["position"] = self.__heuristicCostEstimate(start, goal)
        cameFrom = None

        closedSet = []
        openSet = [start]

        while(not(openSet.empty())):
            # Choose the node with the minimal f score
            openSet = sorted(openSet, key=lambda k: k["f"])
            current = openSet[0]
            
            if current == goal:
                return self.__reconstructPath(cameFrom, current)

            openSet.remove(current)
            closedSet.append(current)
            neighborhood = self.__computeNeighborhood(current)
            for neighbor in neighborhood:
                if neighbor in closedSet:
                    continue

                g = current["g"] + 1
                if openSet.count(neighbor) == 0:
                    openSet.append(neighbor)
                elif g >= neighbor["g"]:
                    continue

                # Best Path Found !
                neighbor["cameFrom"] = current
                neighbor["g"] = g
                neighbor["f"] = neighbor["g"] + self.__heuristicCostEstimate(neighbor, goal)
                
    # A*-related functions
    def __heuristicCostEstimate(self, a, b):  # Euclidian distance
        posA = a["position"]
        posB = b["position"]
        return math.sqrt((posB.getX() - posA.getX())**2 + (posB.getY() - posA.getY())**2)

    def __reconstructPath(self, cameFrom, current):
        path = [current["position"]]
        while current != None:
            current = current["cameFrom"]
            path.append(current["position"])
        
        # Heading command generation
        nodeCount = len(path)
        startHeading = path[0].getHeading()
        goalHeading = path[-1].getHeading()
        
        for i in range(1,nodeCount):
            p = self.__QuintincEaseInOut((i-1)*1.0/nodeCount)
            heading = startHeading + p * (goalHeading - startHeading)
            path[i-1].setHeading(heading)

        self._path = Trajectory(path)
        return path

    def __computeNeighborhood(self, current):
        neighborhood = []
        for j in range(-1,2,1):
            for i in range(-1,2,1):
                nx, ny, nheading = current["position"].getX() + i, current["position"].getY() + j, current["position"].getHeading()
                neighbor = {"position":Position(nx, ny, nheading), "f":math.inf, "g":math.inf, "comeFrom":None}
                if(self.__workingGrid[ny][nx] == 0):
                    neighborhood.append(neighbor)
        return neighborhood

    # Smooth move for heading
    def __QuinticEaseInOut(self, p):    
        if(p < 0.5):
                return 16 * p * p * p * p * p
        else:
                f = ((2 * p) - 2)
                return  0.5 * f * f * f * f * f + 1
