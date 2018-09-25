""" 
	CSI 435: Intro to AI/Machine Learning
	HW 1
	
	Graphs.py: Class containing references of each of the graph types
	by Anita Slater
	
"""

class Graphs:
	g1_vertex = {'S':['d','e','p'],
				 'd':['S','b','c'],
				 'b':['a','d'],
				 'a':['b','c'],
				 'c':['a','d','f'],
				 'e':['d','S','h','r'],
				 'h':['p','e'],
				 'q':['p','h'],
				 'p':['S','h','q'],
				 'r':['e','f'],
				 'f':['r','c','G'],
				 'G':['f'] }

	g2_vertex = {'S':['d','e','p'],
				 'd':['b','c'],
				 'b':['a'],
				 'c':['a'],
				 'e':['h','r'],
				 'h':['q','p'],
				 'p':['q'],
				 'r':['f'],
				 'f':['c','G'] }
g = Graphs()
print(g.g1_vertex)	
