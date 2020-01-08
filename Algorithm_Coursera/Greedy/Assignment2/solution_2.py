from collections import defaultdict
import itertools
#from networkx.utils import UnionFind

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
        if lx != ly:
            self.leader_to_vertex[lx] = [*self.leader_to_vertex[lx], *self.leader_to_vertex[ly]]
            for v in self.leader_to_vertex[ly]:
                self.vertex_to_leader[v] = lx
            del self.leader_to_vertex[ly]



class Clustering_big(object):
    def __init__(self, filename, max_dist):
        # load data, read bits into integer
        self.nodes = self.load_data(filename)
        self.nodes_idx = [i for i in range(self.num_nodes)]
        # mapping the integer value with node index
        self.int_to_idx = defaultdict(list)
        for i, n in enumerate(self.nodes):
            self.int_to_idx[n].append(i)

        self.u = Union_structure(self.nodes_idx)

        masks = self.bit_masks_within_max_dist(self.num_bits, max_dist)
        print(len(masks))
        for key in self.int_to_idx.keys():
            for mask in masks:
                found = self.int_to_idx.get(key ^ mask, None)
                if found != None:
                    temp = [*self.int_to_idx[key], *found]
                    for i in range(1, len(temp)):
                        self.u.union(temp[0], temp[i])
            print(len(self.u.leader_to_vertex))
                
                
    def load_data(self, filename):
        file = open(filename, "r") 
        data = file.readlines()

        num_nodes, num_bits = data.pop(0).split(' ')
        self.num_nodes = int(num_nodes)
        self.num_bits = int(num_bits)

        nodes = [0 for i in range(self.num_nodes)]
       
       # convert bit string to integer values
        for i, line in enumerate(data):
            bits = line.split(' ')
            bits = "".join(bits[:self.num_bits]) # take out \n characters at the end
            nodes[i] = int(bits, 2)
        
        return nodes

    # Bitmasks for Hamming distance
    # print(bit_masks(3,1))  [1, 2, 4]
    # print(bit_masks(4,2))  [3, 5, 9, 6, 10, 12]
    # print(bit_masks(4,3))  [7, 11, 13, 14]
    def bit_masks(self, num_bits, distance):
        combos = itertools.combinations(range(num_bits), distance)
        masks = []
        for idx_pairs in combos:
            temp = 0
            for idx in idx_pairs:
                temp = (1 << idx) ^ temp
            masks.append(temp)
        return masks
    
    def bit_masks_within_max_dist(self, num_bits, max):
        masks = [0]
        for i in range(1, max+1):
            temp = self.bit_masks(num_bits, i)
            masks = [*masks, *temp]
        return masks



if __name__=="__main__":
    g = Clustering_big("clustering_big.txt", 2)
    print(len(g.u.leader_to_vertex))