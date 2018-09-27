"""
	CSI 435: Intro to AI/Machine Learning
	HW 1

	algos.py: Class containing references of each of the algorithms
	by Anita Slater

"""
import numpy as np
from data import Data

test=Data()

def dfs_recursive(graph, node, goal, visited):
    #print("@",node,"@", end="")
    visited.append(node)
    if node == goal:
        print("BOOM")
        return visited
    for n in graph[node]:
        #print(graph[node],"->{",n,"}")
        if n not in visited:
            #print("{{",n,"}}->",end="")
            dfs_recursive(graph,n,goal,visited)
    return visited

def dfs_stack(graph, start, goal,visited):
    stack=[start]
    while stack:
        n=stack.pop(0)
        if n not in visited:
            visited = visited + [n]
            stack=graph[n]+stack
    return visited

def bfs_stack(graph,start,visited):
    stack=[start]
    while stack:
        n=stack.pop(0)
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
    return visited

graph=test.test1

print(dfs_recursive(graph,'A','G',[]))
print(dfs_stack(graph,'A','G',[]))
print(bfs_stack(graph,'A',[]))

