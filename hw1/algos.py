"""
	CSI 435: Intro to AI/Machine Learning
	HW 1

	algos.py: Class containing references of each of the algorithms
	by Anita Slater

"""
import numpy as np
from data import Data

test=Data()

def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_recursive(graph,n,visited)
    return(visited)

def dfs_stack(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def r_test(graph,node,end,visited):
    if node not in visited:
        visited.append(node)
        if node != end:
            for n in graph:
                if n != end:
                    r_test(graph,n,end,visited)
                else:
                    if n not in visited:
                        visited.append(n)
                    return visited
    return visited
                #visited = dfs_recursive(test.test,'S', [])
graph=test.g1_vertex

print(r_test(graph,'S','G',[]))
#(dfs_recursive(graph,'S',[]))
#list(dfs_stack(graph,'S','G'))


# # Transform Vertex-List to Adjacency Matrix
# def vertex_list_2_matrix(vertex_graph):
#     n = len(vertex_graph)
#     adj_matrix = np.nan * np.ones((n, n))
#     np.fill_diagonal(adj_matrix, 0)
#
#     for i in range(n):
#         for j, w in vertex_graph[i]:
#             adj_matrix[i, j] = w
#             return adj_matrix
#
# #print(g1.g1_vertex)
# print(vertex_list_2_matrix(g1.g1_vertex))
#
