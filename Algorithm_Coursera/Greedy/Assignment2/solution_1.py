# Kruskal's MST algorithm with Union-Find Data Structure

from collections import defaultdict

class Union_structure(object):
    def __init__(self, vertex):
        self.vertex_to_leader = dict()
        self.leader_to_vertex = defaultdict(list)

        for v in vertex:
            self.vertex_to_leader[v] = v
            self.leader_to_vertex[v].append(v)

    def find(self, x):
        return self.vertex_to_leader[x]
        
    def union(self, x, y):
        lx = self.find(x)
        ly = self.find(y)
        self.leader_to_vertex[lx] = [*self.leader_to_vertex[lx], *self.leader_to_vertex[ly]]
        for v in self.leader_to_vertex[ly]:
            self.vertex_to_leader[v] = lx
        del self.leader_to_vertex[ly]


class Kruskal_Clustering(object):
    def __init__(self, filename):
        # load data // v1, v2, cost
        self.edges = self.load_data(filename)
        
        # sort edges by cost
        sorted_idx = sorted(range(len(self.edges)), key = lambda k: self.edges[k][2])
        sorted_edges = []
        for idx in sorted_idx:
            sorted_edges.append(self.edges[idx])
        self.edges = sorted_edges
        
        # extract vertex from edges
        self.vertex = set()
        for edge in self.edges:
            self.vertex.add(edge[0])
            self.vertex.add(edge[1])
        self.vertex = list(self.vertex)

        # set Union data structure
        self.u = Union_structure(self.vertex)

    def find_max_spacing(self, k=4):
        # iterate through edges
        max = None
        for edge in self.edges:
            if len(self.u.leader_to_vertex) >= k:
                if self.u.find(edge[0]) != self.u.find(edge[1]):
                    self.u.union(edge[0],edge[1])
                max = edge
            else:
                break
        
        return max
        
    def load_data(self, filename):
        file = open(filename, "r") 
        data = file.readlines()
        self.num_nodes = int(data[0])
        edges = []
        for i in range(1, len(data)):
            line = data[i].split(" ")
            edges.append([int(line[0])-1, int(line[1])-1, int(line[2])])
        return edges

if __name__=="__main__":
    g = Kruskal_Clustering('216.txt')
    print(g.find_max_spacing(4))
    k = Kruskal_Clustering('90.txt')
    print(k.find_max_spacing(4))
    l = Kruskal_Clustering('clustering1.txt')
    print(l.find_max_spacing(4))