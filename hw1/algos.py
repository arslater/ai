"""
	CSI 435: Intro to AI/Machine Learning
	HW 1

	algos.py: Class containing references of each of the algorithms
	by Anita Slater

"""
from data import Data
import queue as Q

def dfs_recursive(graph, node, goal, visited):
    visited.append(node)
    if node == goal:
        return visited
    for n in graph[node]:
        if n not in visited:
            dfs_recursive(graph,n,goal,visited)
    return visited

def dfs_recursive_matrix(graph, node, goal, visited):
    visited.append(node)
    if node == goal:
        return visited
    for n in graph[node]:
        if n not in visited:
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

def ucs_vertex(graph, root, goal):
    pq=Q.PriorityQueue()
    weight = 0
    visited = []
    path = []
    parents = {root:None}

    fringe=graph[root]
    pq.put((weight,root))

    while not pq.empty():
        dq_item=pq.get()
        cur_node=dq_item[1]
        cur_node_weight=dq_item[0]

        if cur_node == goal:
            path = [cur_node]
            prev_node = cur_node

            while prev_node != root:
                parent = parents[prev_node]
                path.append(parent)
                prev_node = parent

            path.reverse()
            return (visited,path)
        else:
            for edge,key in graph[cur_node].items():
                child = edge

                if child not in visited:
                    visited.append(child)
                    parents[child] = cur_node
                    pq.put((weight+key,child))

def vert_2_matrix_2(graph):
    entries=[]
    row=[]
    columns=[]
    for node in graph:
        entries.append(node)
    for node in graph:
        for entry in entries:
            if entry in graph[node]:
                row.append("1")
            else:
                row.append("0")
        columns.append(row)
        row=[]
    return columns