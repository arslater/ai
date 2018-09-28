"""
	CSI 435: Intro to AI/Machine Learning
	HW 1

	Graphs.py: Class containing references of each of the graph types
	by Anita Slater

"""
import numpy as np


class Data:

    g1_vertex = {}
    g2_vertex = {}
    test      = {}

    def __init__(self):
        self.g1_vertex = {'S': ['d', 'e', 'p'],
                 'd': ['S', 'b', 'c', 'e'],
                 'b': ['a', 'd'],
                 'a': ['b', 'c'],
                 'c': ['a', 'd', 'f'],
                 'e': ['d','h', 'r','S'],
                 'h': ['e','p','q'],
                 'q': ['h','p'],
                 'p': ['h', 'q','S'],
                 'r': ['e', 'f'],
                 'f': ['c', 'G','r'],
                 'G': ['f']}

        self.g2_vertex={'S': ['d', 'e', 'p'],
                 'd': ['b', 'c'],
                 'b': ['a'],
                 'c': ['a'],
                 'e': ['h', 'r'],
                 'h': ['q', 'p'],
                 'p': ['q'],
                 'r': ['f'],
                 'f': ['c', 'G']}

        self.g3_vertex = {'S': {'d':3, 'e':9, 'p':1},
                          'd': {'S':3, 'b':1, 'c':8, 'e':2},
                          'b': {'a':2, 'd':1},
                          'a': {'b':2, 'c':2},
                          'c': {'a':2, 'd':8, 'f':3},
                          'e': {'d':2, 'h':8, 'r':2, 'S':9},
                          'h': {'e':8, 'p':4, 'q':4},
                          'q': {'h':4, 'p':15},
                          'p': {'h':4, 'q':15, 'S':1},
                          'r': {'e':2, 'f':2},
                          'f': {'c':3, 'G':2, 'r':2},
                          'G': {'f':2}}

        self.g4_vertex={'S':{'d':3, 'e':9, 'p':1},
                 'd': {'b':1, 'c':8},
                 'b': {'a':2},
                 'c': {'a':2},
                 'e': {'h':8, 'r':2},
                 'h': {'q':4, 'p':4},
                 'p': {'q':15},
                 'r': {'f':2},
                 'f': {'c':3, 'G':2}}

        self.test={'S': ['A','B','D'],
                   'A': ['C','S'],
                   'C': ['A','D','G'],
                   'G': ['C','D'],
                   'D': ['B','C','G','S'],
                   'B': ['D','S']}
        self.test1={'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
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


