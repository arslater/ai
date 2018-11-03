##########################
## CEN 535: Inro to AI -- HW2
##
## graphs.py: Creating a graph class to make 
##				  graph and node modification easier.
## by Anita Slater
##########################

class Node():
    def __init__(self, node):
        self.name=node
        self.adjacent = {}
        self.heuristic=0

    def addNeighbor(self,neighbor,weight=0): 
        self.adjacent[neighbor] = weight

    def getNeighbors(self): 
        return self.adjacent.keys()

    def getName(self):
        return self.name

    def getWeight(self,neighbor):
        return self.adjacent[neighbor]

    def __lt__(self,other):
        return self.heuristic < other.heuristic
		  ## tie breaker, favors the current node

class Graph(object):
    def __init__(self):
        self.nodes={}
        self.NumberOfNodes = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def addNode(self,node,heuristic):
        self.NumberOfNodes += 1
        newNode = Node(node)
        self.nodes[node] = newNode
        newNode.heuristic=heuristic

        return newNode

    def addEdge(self,to,frm,weight=0):
        if frm not in self.nodes:
            self.addNode(frm,0)
        if to not in self.nodes:
            self.addNode(to,0)

        self.nodes[to].addNeighbor(self.nodes[frm],weight)
        self.nodes[frm].addNeighbor(self.nodes[to],weight)

    def getNodes(self):
        return self.nodes.keys()

    def getVertex(self,n):
        if n in self.nodes:
            return self.nodes[n]
        else:
            print("ERROR: Vertex not in graph")
            return None


def g2():
	## Creating the graph in the problem
    g = Graph()

    g.addNode('S',0)
    g.addNode('b',7)
    g.addNode('p',14)
    g.addNode('d',7)
    g.addNode('a',5)
    g.addNode('c',4)
    g.addNode('q',12)
    g.addNode('h',11)
    g.addNode('e',5)
    g.addNode('r',3)
    g.addNode('f',2)
    g.addNode('G',0)

    g.addEdge('S','d',3)
    g.addEdge('S','e',9)
    g.addEdge('S','p',1)
    g.addEdge('d','b',1)
    g.addEdge('d','c',8)
    g.addEdge('d','e',2)
    g.addEdge('b','a',2)
    g.addEdge('a','c',2)
    g.addEdge('c','f',3)
    g.addEdge('e','h',8)
    g.addEdge('e','r',2)
    g.addEdge('h','p',4)
    g.addEdge('h','q',4)
    g.addEdge('q','p',15)
    g.addEdge('r','f',2)
    g.addEdge('f','G',2)

    return g


