##########################
## CEN 535: Inro to AI -- HW2
##
## main.py: Contains the output for each function in hw2
## by Anita Slater
##########################
from graphs1 import *
from graph import *
from astar import *
from greedy import greedy
from minimax import *
import sys

#################
## Q1: Informed Search

##
## Q1.1: Greedy Search
print("Q1.1 -- Greedy Search:")
print("States Expanded:",greedy('S','G',g1)[0])
print("Path Returned:",greedy('S','G',g1)[1])
print()

## Q1.2: A* Search
path,states = astar_search(graph.getVertex('S'),'G', graph)

print("Q1.2 -- A* Search:")
print("States Expanded:[", end='')
for state,weight in states.items():
    print("'",state,"', ",end="",sep="")
print("\b\b]\nPath Returned: [",end='')

for state,time in path.items():
    print("'",state.getName(),"', ",end="",sep='')
print("\b\b]\n")

####################3
## Q3: Adversarial Search

## 1:
values=[3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]
treeDepth=math.log(len(values),2)

value,path=minimax(0,0,True,values,treeDepth,[])

print("Q3.1 -- Adversarial Search with Minimax")
print("Output Path: ",path)
print("Output Value: ",value,"\n")

## 3:
valueab=minimaxab(values,0,True,treeDepth,0,[],10000,-10000)

print("Q3.3 -- Adversarial Search with Minimax & Alpha-Beta Pruning")
print("Output Value: ",valueab)
