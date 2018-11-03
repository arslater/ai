##########################
## CEN 535: Inro to AI -- HW2
##
## algos.py: Contains the greedy-search algorithm
## by Anita Slater
##########################

from graph import g1
import queue as Q

def greedy_algo(start, end, graph,visited):
    visited.append(start)
    fringe = []

    if start == end:
        return visited

    for node,weight in graph[start].items():
        shortestPath=min(graph[start].values())
        print(shortestPath,"VERSUS",weight)
        if(node not in visited and weight == shortestPath):
            print("DINGDINGDING")
            greedy_algo(node,'G',graph,visited)

    return visited

#print((greedy_algo('S','G',g1,[])))

## Trying greedy search as a priority queue

def greedy(root,goal,graph):
    pq = Q.PriorityQueue()
    weight = 0
    visited = []
    path = []
    parents = {root: None}

    fringe = graph[root]
    pq.put((weight, root))

    while not pq.empty():
        dq_item = pq.get()
        cur_node = dq_item[1]
        cur_node_weight = dq_item[0]

        if cur_node == goal:
            path = [cur_node]
            prev_node = cur_node

            while prev_node != root:
                parent = parents[prev_node]
                path.append(parent)
                prev_node = parent

            path.reverse()
            return (visited, path)
        else:
            for edge, key in graph[cur_node].items():
                child = edge

                if child not in visited:
                    visited.append(child)
                    parents[child] = cur_node
                    pq.put((weight + key, child))
#print(greedy('S','G',g1))