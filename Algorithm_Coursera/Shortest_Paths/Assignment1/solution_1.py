# Bellman-Ford iterative
# Check negative cycle
from collections import defaultdict
import math

class Bellman_Ford_iter(object):
    def __init__(self, filename, start_v):
        file = open(filename, "r") 
        # [number of vertices][number of edges]
        # [head] [tail] [length]
        data = file.readlines()
        no_vertices = int(data[0].split(" ")[0])
        no_edges = int(data[0].split(" ")[1])
        edges = defaultdict(list)
        for i in range(1, no_edges+1):
            line = data[i].split(" ")
            edges[int(line[0])].append((int(line[1]), int(line[2]))) 
            # key: head, value: (tail, length)

        A = [[math.inf for n in range(no_vertices+1)] for i in range(no_edges+1)]
        for i in range(no_edges+1):
            A[i][start_v] = 0

        for i in range(1, no_edges+1):
            print("checkpoint", i)
            for v in range(1, no_vertices+1):
                a1 = A[i-1][v]
                a2 = []
                for w, c in edges.get(v, []):
                    a2.append(A[i-1][w] + c)
                a2 = min(a2)
                A[i][v] = min(a1, a2)
        
        self.has_negative_edges = 0
        for v in range(1, no_vertices):
            self.has_negative_edges += ( A[no_edges-1][v] - A[no_edges][v] )
        


g1 = Bellman_Ford_iter("g1.txt", 1)
print(g1.has_negative_edges) # negative cycle

g2 = Bellman_Ford_iter("g2.txt", 1)
print(g2.has_negative_edges) # negative cycle

g3 = Bellman_Ford_iter("g3.txt", 1)
print(g3.has_negative_edges)