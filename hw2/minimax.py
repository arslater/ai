##########################
## CEN 535: Inro to AI -- HW2
##
## minimax.py: Contains the code for the Minimax Algorithm
## by Anita Slater
##########################
from binTree import *
import math

def minimax(curDepth,index,maxTurn,values,targetDepth,visited):
    if values[index] not in visited:
        visited.append(values[index])
    #print(values[index])
    if curDepth == targetDepth:
        return values[index],visited
    if maxTurn:
        #print("Maximzing",values[index*2],"vs",values[index*2+1])
        return max(minimax(curDepth+1, index*2,False,
                           values,targetDepth,visited),
                   minimax(curDepth+1,index*2+1,False,
                            values,targetDepth,visited))
    else:
        #print("Minimizing", values[index * 2], "vs", values[index * 2 + 1])
        return min(minimax(curDepth + 1, index * 2, True,
                           values, targetDepth,visited),
                   minimax(curDepth + 1, index * 2 + 1, True,
                           values, targetDepth,visited))

def minimaxab(values,index,maxTurn,targetDepth,curDepth,visited,alpha,beta):
    if values[index] not in visited:
        visited.append(values[index])
    if curDepth == targetDepth:
        return values[index]

    if maxTurn:

        best = -10000
        for i in range(0,2):
            val = minimaxab(values,index*2,False,
                            targetDepth,curDepth+1,[],
                            alpha,beta)

            best  = max(best,val)
            alpha = max(alpha,best)

            ## Actual pruning here, if the best possible
            ## value is smaller than the alpha, skip
            ## the rest of this leaf
            if (beta <= alpha):
                break
        return best
    else:

        best = 10000
        for i in range(0, 2):
            val = minimaxab(values, index * 2, True,
                            targetDepth, curDepth + 1,[],
                            alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            ## Actual pruning here, if the best possible
            ## value is smaller than the alpha, skip
            ## the rest of this leaf
            if (beta <= alpha):
                break
        return best

values=[3, 10, 2, 9, 10, 7, 5, 9, 2, 5, 6, 4, 2, 7, 9, 1]
targetDepth=math.log(len(values),2)
print(minimaxab(values,0,True,targetDepth,0,[],10000,-10000))
