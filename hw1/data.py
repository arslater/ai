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

        self.test={'S': ['A','B','D'],
                   'A': ['C','S'],
                   'C': ['A','D','G'],
                   'G': ['C','D'],
                   'D': ['B','G','S'],
                   'B': ['D','S']}
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


