""" 
	CSI 435: Intro to AI/Machine Learning
	HW 1
	
	Graphs.py: Class containing references of each of the graph types
	by Anita Slater
	
"""

class Graphs:
	g1_vertex = {'S':['d','e','p'],
				 'd':['S','b','c','e'],
				 'b':['a','d'],
				 'a':['b','c'],
				 'c':['a','d','f'],
				 'e':['d','S','h','r'],
				 'h':['p','e','q'],
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

	""" Adjacency Matrices

	G1:
		S a b c d e f h p q r G
	  S 0 0 0 0 1 1 0 0 0 1 0 0
	  a 0 0 1 1 0 0 0 0 0 0 0 0
      b 0 1 0 0 1 0 0 0 0 0 0 0
      c 0 1 0 0 1 0 1 0 0 0 0 0 
      d 1 0 1 1 0 1 0 0 0 0 0 0
      e 1 0 0 0 1 0 0 1 0 0 1 0
      f 0 0 0 1 0 0 0 0 0 0 1 1
      h 0 0 0 0 0 1 0 0 1 1 0 0
      p 1 0 0 0 0 0 0 1 0 1 0 0
      q 0 0 0 0 0 0 0 1 1 0 0 0
      r 0 0 0 0 0 1 1 0 0 0 0 0
      G	0 0 0 0 0 0 1 0 0 0 0 0
	
	"""


g = Graphs()
print(g.g1_vertex)	
