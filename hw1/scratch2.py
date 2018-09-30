from data import Data
import queue as Q

test=Data()

def ucs(graph, node, goal):
    queue=Q.PriorityQueue()
    path = {}
    visited = []            ## Basic variables for algorithm
    fringe = {} # fringe nodes
    prev_node = node
    i = 0

    #print(graph[node])

    for entry in graph.values():
        print(entry)
        shortest_fringe = min(entry.values())
        #print(shortest_fringe)
        for fringe_node, key in entry.items():
            #print("weight:",key,"value:",fringe_node)
            if key == shortest_fringe:
                print("smallest value: ", shortest_fringe, "node:",fringe_node)
    if node == goal:
        return path

ucs(test.g3_vertex,'S', 'G')