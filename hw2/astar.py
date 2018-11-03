##########################
## CEN 535: Inro to AI -- HW2
##
## astar.py: Contains the code for the A* Algorithm
## by Anita Slater
##########################

import queue as Q
from graphs1 import *

graph=g2()

def astar_search(root,goal,graph):

    openSet   = Q.PriorityQueue() # nodes to examine (frontier)
    closedSet = {}  # examined nodes (interior)
    cost      = {}

    openSet.put((0,root))
    cost[root.getName()] = 0
    
    while openSet:
        currNode = openSet.get()[1]

        if currNode.getName() == goal:
            closedSet[currNode] = currNode
            break

        for next in currNode.getNeighbors():
            newCost = cost[currNode.getName()] + currNode.getWeight(next)
            if next.getName() not in cost or newCost < cost[next.getName()]:
                cost[next.getName()] = newCost
                priority = newCost + next.heuristic
                openSet.put((priority,next))
                closedSet[currNode] = currNode

    return closedSet,cost