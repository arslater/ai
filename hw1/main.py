from algos import *

class main:

    g1_vertex = Data().g1_vertex
    g1_matrix  = vert_2_matrix_2(g1_vertex)

    g2_vertex = Data().g2_vertex
    g2_matrix = vert_2_matrix_2(g2_vertex)

    g3_vertex = Data().g3_vertex
    g3_matrix = vert_2_matrix_2(g3_vertex)

    g4_vertex = Data().g4_vertex
    g4_adjac = vert_2_matrix_2(g4_vertex)

    print("G1: DFS Vertex-List w/ Recursion:")
    print("    States Expanded:",dfs_recursive(g1_vertex,'S','G',[]))
    print("    Path Returned: ")
    print()


    print("G1: DFS Vertex-List w/ Stack:")
    print("    States Expanded:", dfs_stack(g1_vertex, 'S', 'G', []))
    print("    Path Returned: " )
    print()

    print("G2: DFS Vertex-List w/ Recursion:")
    print("    States Expanded:", dfs_recursive(g2_vertex, 'S', 'G', []))
    print("    Path Returned: ", )
    print()

    print("G2: DFS Vertex-List w/ Stack:")
    print("    States Expanded:", dfs_stack(g2_vertex, 'S', 'G', []))
    print("    Path Returned: ", )
    print()

    print("G1: BFS Vertex-List")
    print("    States Expanded:", bfs_stack(g1_vertex, 'S', []))
    print("    Path Returned: ", )
    print()

    print("G2: BFS Vertex-List")
    print("    States Expanded:", bfs_stack(g2_vertex, 'S', []))
    print("    Path Returned: ", )
    print()

    print("G3: UCS Vertex-List")
    ucs=ucs_vertex(g3_vertex, 'S','G')
    print("    States Expanded:", ucs[0])
    print("    Path Returned: ", ucs[1])
    print()

    print("G4: UCS Vertex-List")
    ucs = ucs_vertex(g4_vertex, 'S', 'G')
    print("    States Expanded:", ucs[0])
    print("    Path Returned: ", ucs[1])
    print()

