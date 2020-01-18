# Floyd-Warshall Algorithm
# Compute all pairs shortest path
 
from collections import defaultdict
import math
import sys
sys.setrecursionlimit(5000)

class Floyd_Warshall(object):
    def __init__(self, filename):
        file = open(filename, "r") 
        # [number of vertices][number of edges]
        # [head] [tail] [length]
        data = file.readlines()
        self.no_vertices = int(data[0].split(" ")[0])
        self.no_edges = int(data[0].split(" ")[1])
        self.edge_to_cost = dict()
        for i in range(1, self.no_edges):
            line = data[i].split(" ")
            self.edge_to_cost[(int(line[0]), int(line[1]))] = int(line[2])

        self.A = {}

        for v in range(1, self.no_vertices+1):
            for w in range(1, self.no_vertices+1):
                if v == w:
                    self.A[(v,w)] = 0
                else:
                    len_vw = self.edge_to_cost.get((v,w))
                    if len_vw != None:
                        self.A[(v,w)] = len_vw
                    else:
                        self.A[(v,w)] = math.inf
        self.B = self.recursive(self.A, 1)
    def recursive(self, A, k):
        B = {}
        print(k)
        if k == self.no_vertices:
            return A
        for v in range(1, self.no_vertices+1):
            for w in range(1, self.no_vertices+1):
                B[(v,w)] = min(A[(v,w)], A[(v,k)] + A[(k,w)])
        
        A.clear()
        return self.recursive(B, k+1)
        

        # for v in range(1, no_vertices+1):
        #     if A[no_vertices][v][v] < 0:
        #         self.result = "negative"


g3 = Floyd_Warshall("g3.txt")
print(min(list(g3.B.values()))) # -19