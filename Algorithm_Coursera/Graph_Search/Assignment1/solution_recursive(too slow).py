from collections import defaultdict

class Solution(object):
    def __init__(self, file, sep):
        
        self.edges = []
        

        with open(file, 'r') as f:
            for str in f:
                line = [int(s) for s in str.rstrip().split(sep)]
                self.edges.append(line)
        
        self.vectors = set()
        for edge in self.edges:
            for vector in edge:
                self.vectors.add(vector)
    
        self.unexplored_vectors = set()
        
        self.current_label = 0

    # def depth_first_search(self):
    # mark all vertices as unexplored
    # S = a stack data structure, init with s
    # While S is not empty
    #   remove(pop) the vertex v from the front of S
    #   if v is unexplored
    #       mark v as explored
    #       for each edge(v,w) in v's adjacency list
    #           add(push) w to the front of S

    def depth_first_search(self, reversed = False):
        stack = []
        explored_vectors = []
        self.unexplored_vectors = {*self.vectors}
        starting_vector = 0
        for s in self.unexplored_vectors:
            starting_vector = s
            break
        stack.append(starting_vector)

        while len(stack)>0 :
            v = stack.pop()
            if v in self.unexplored_vectors:
                self.unexplored_vectors.remove(v)
                explored_vectors.append(v)
                for edge in self.edges:
                    if edge[0^reversed] == v:
                        stack.append(edge[1^reversed])
        
        return explored_vectors
    
    def topo_sort(self):
        current_label = len(self.vectors)
        self.unexplored_vectors = {*self.vectors}
        self.f = defaultdict(int)

        for vector in self.vectors:
            if vector in self.unexplored_vectors:
                current_label = self.dfs_topo(vector, current_label)

    def dfs_topo(self, vector, current_label):
        self.unexplored_vectors.discard(vector)
        self.f[vector] = current_label
        current_label -= 1
        for edge in self.edges:
            if edge[1] == vector:
                if edge[0] in self.unexplored_vectors:
                    current_label = self.dfs_topo(edge[0], current_label)
        return current_label
    
    def find_scc(self):
        self.unexplored_vectors = {*self.vectors}
        sccIdx = 0
        scc = defaultdict(list)
        inv_f = {v: k for k, v in self.f.items()}
        keys = list(inv_f.keys())
        keys.sort(reverse=False)

        first = inv_f[keys[0]]
        check_list = []
        unsafe = True
        for edge in self.edges:
            if edge[0] == first:
                check_list.append(edge[1])
        for vector in check_list:
            for edge in self.edges:
                if edge[0] == vector and edge[1] == first:
                    unsafe = False
        if unsafe:
            keys.pop(0)
            scc[sccIdx].append(first)

        for key in keys:
            vector = inv_f[key]
            if vector in self.unexplored_vectors:
                sccIdx += 1
                print(sccIdx)
                scc = self.dfs_scc(vector, scc, sccIdx)
        return scc
        
    def dfs_scc(self, vector, scc, sccIdx):
        scc[sccIdx].append(vector)
        self.unexplored_vectors.remove(vector)
        for edge in self.edges:
            if edge[0] == vector:
                if edge[1] in self.unexplored_vectors:
                    self.dfs_scc(edge[1], scc, sccIdx) 
        return scc


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**5)

    test1 = Solution("test1.txt", " ")
    print(test1.depth_first_search()) # [1, 3, 11, 8, 6, 10, 5, 9, 4, 7, 2]
    test1.topo_sort()
    print(test1.f) # defaultdict(<class 'int'>, {1: 11, 5: 10, 3: 9, 2: 8, 9: 7, 7: 6, 4: 5, 6: 4, 8: 3, 10: 2, 11: 1})
    dict = test1.find_scc()
    len_array = []
    for scc in dict.values():
        len_array.append(len(scc))
    len_array.sort(reverse=True)
    print(len_array) # [4, 4, 3, 1]


    test2 = Solution("SCC.txt", " ")
    test2.topo_sort()
    dict2 = test2.find_scc()
    len_array2 = []
    for scc in dict2.values():
        len_array2.append(len(scc))
    len_array2.sort(reverse=True)
    print(len_array2)
