##########################
## CEN 535: Inro to AI -- HW2
##
## main.py: Contains the main funciton
## by Anita Slater
##########################
from graphs1 import *
from graph import *
from astar import *
from algos import greedy
import sys

###########
## Q1: Greedy Search
print("Q1 -- Greedy Search:")
print("States Expanded: ",greedy('S','G',g1)[0])
print("Path Returned:",greedy('S','G',g1)[1])
print()
###########
## Q2: A* Search
path,states = astar_search(graph.getVertex('S'),'G', graph)

print("Q2 -- A* Search:")
print("States Expanded:[ ", end='')
for state,weight in states.items():
    print("'",state,"', ",end="",sep="")
print("]\n Path Returned: [",end='')

for state,time in path.items():
    print("'",state.getName(),"', ",end="",sep='')
print(" ]")