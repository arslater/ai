##########################
## CEN 535: Inro to AI -- HW2
##
## graphs.py: Holds the hard-coded adjacency lists
##            of graphs used in this program.
## by Anita Slater
##########################

g3_vertex = {'S': {'d':3, 'e':9, 'p':1},
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