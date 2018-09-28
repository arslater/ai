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
def ucs_vertex():
    print("https://stackoverflow.com/questions/43354715/uniform-cost-search-in-python")

def vert_2_matrix_2(graph,start):
    row=[]
    for node in graph:
        row.append(node)
    for node in graph:
        for entry in row:
            if entry in graph[node]:
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()
graph=test.test

print(dfs_recursive(graph,'S','G',[]))
print(dfs_stack(graph,'S','G',[]))
print(bfs_stack(graph,'S',[]))

