##########################
## CEN 535: Inro to AI -- HW2
##
## astar.py: Contains the code for the A* Algorithm
## by Anita Slater
##########################

# import heapq
#
#
# class PriorityQueue:
#     def __init__(self):
#         self.elements = []
#
#     def empty(self):
#         return len(self.elements) == 0
#
#     def put(self, item, priority):
#         heapq.heappush(self.elements, (priority, item))
#
#     def get(self):
#         return heapq.heappop(self.elements)[1]
#
# from astar import PriorityQueue
import queue as Q
from graphs1 import *

graph=g2()

def astar_search(root,goal,graph):

    openSet   = Q.PriorityQueue() # nodes to examine (frontier)
    closedSet = {}  # examined nodes (interior)
    cost      = {}

    openSet.put((0,root))
    cost[root.getName()] = 0
    #closedSet[root.getName()] = None

    #print(openSet.get()[1].getName())
    i =0

    while openSet:
        currNode = openSet.get()[1]
        #print("**",currNode.getName())

        #exit(1)
        if currNode.getName() == goal:
            closedSet[currNode] = currNode
            break
        csno = None

        for next in currNode.getNeighbors():
            #print(next.getName(),cost[currNode.getName()])
            newCost = cost[currNode.getName()] + currNode.getWeight(next)
            if next.getName() not in cost or newCost < cost[next.getName()]:
                cost[next.getName()] = newCost
                priority = newCost + next.heuristic
                #print("%%",priority)
                #print(":)")
                openSet.put((priority,next))

                #if currNode not in closedSet:
                closedSet[currNode] = currNode

                i+=1
    return closedSet,cost

#
# for node, time in cost.items():
#     print(node)
# print()
#
# for node in close.values():
#     print(node.getName())
##    print(val[0].get()[1].getName())

#print(graph.nodes['S'].getName())