##########################
## CEN 535: Inro to AI -- HW2
##
## minimax.py: Contains the code for the Minimax Algorithm
## by Anita Slater
##########################
from binTree import *
import math

def minimax(curDepth,index,maxTurn,values,targetDepth):
    if curDepth == targetDepth:
        return values[index]
    if maxTurn:
        return max(minimax(curDepth+1, index*2,False,
                           values,targetDepth),
                   minimax(curDepth+1,index*2+1,False,
                            values,targetDepth))
    else:
        return min(minimax(curDepth + 1, index * 2, True,
                           values, targetDepth),
                   minimax(curDepth + 1, index * 2 + 1, True,
                           values, targetDepth))


values=[3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]

treeDepth=math.log(len(values),2)
print(minimax(0,0,True,values,treeDepth))



