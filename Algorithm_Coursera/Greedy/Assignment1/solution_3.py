# Prim's Minimum Spanning Tree 

import random
from collections import defaultdict

# Load Data
filename = 'edges.txt'
file = open(filename, "r") 
data = file.readlines()
num_nodes = int(data[0].split(' ')[0])
num_edges = int(data[0].split(' ')[1])
raw_edge_data = [[] for i in range(0, num_edges)]
edges = defaultdict(list)

for i in range(0, num_edges):
    line = data[i+1].split(' ')
    edges[int(line[0])-1].append([i, int(line[1])-1, int(line[2])]) # T index, v, cost
    edges[int(line[1])-1].append([i, int(line[0])-1, int(line[2])]) # T index, v, cost
    raw_edge_data[i] = [int(line[0])-1, int(line[1])-1, int(line[2])]

T = [False for i in range(0, num_edges)]
V = [i for i in range(0, num_nodes)]
X = []
u = random.choice(V)
X.append(u)
V.remove(u)

while len(V)>0:
    print(len(V))
    collect = []
    for i in range(len(edges)):
        for e in edges[i]:
            if (i in X and e[1] in V):
                collect.append(e)

    if len(collect) > 0 :
        sorted_idx = sorted(range(len(collect)), key = lambda k: collect[k][2])
        idx = collect[sorted_idx[0]][0]
        v = collect[sorted_idx[0]][1]
        T[idx] = True
        X.append(v)
        V.remove(v)

cost = 0
for i in range(len(T)):
    if T[i] == True:
        cost = cost + raw_edge_data[i][2]

print("Cost", cost) # -3612829
