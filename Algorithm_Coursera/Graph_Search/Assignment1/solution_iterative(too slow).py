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
    
    def topo_sort(self, reversed = True):
        current_label = len(self.vectors)
        self.f = defaultdict(int)

        self.unexplored_vectors = {*self.vectors}
        stack = []
        for start in self.vectors:
            if start in self.unexplored_vectors:
                stack.append(start)
                while len(stack)>0 :
                    v = stack.pop()
                    if v in self.unexplored_vectors:
                        self.f[v] = current_label
                        current_label -= 1
                        self.unexplored_vectors.remove(v)
                        for edge in self.edges:
                            if edge[0^reversed] == v:
                                stack.append(edge[1^reversed])

    def find_scc(self):
        self.unexplored_vectors = {*self.vectors}
        sccIdx = 0
        scc = defaultdict(list)
        inv_f = {v: k for k, v in self.f.items()}
        keys = list(inv_f.keys())
        keys.sort(reverse=False)

        stack = []
        for key in keys:
            start = inv_f[key]
            if start in self.unexplored_vectors:
                stack.append(start)
                sccIdx += 1
                while len(stack)>0 :
                    v = stack.pop()
                    if v in self.unexplored_vectors:
                        scc[sccIdx].append(v)
                        self.unexplored_vectors.remove(v)
                        for edge in self.edges:
                            if edge[0] == v:
                                stack.append(edge[1])        
        return scc
        

if __name__ == "__main__":

    test1 = Solution("test1.txt", " ")
    test1.topo_sort()
    print(test1.f)
    # {1: 11, 5: 10, 3: 9, 2: 8, 9: 7, 7: 6, 4: 5, 6: 4, 11: 3, 8: 2, 10: 1}
    dict = test1.find_scc()
    len_array = []
    for scc in dict.values():
        len_array.append(len(scc))
    len_array.sort(reverse=True)
    print(dict) # {1: [10, 8, 6], 2: [11], 3: [4, 7, 9, 2], 4: [3, 5, 1]})
    print(len_array) # [4, 4, 3, 1]


    test2 = Solution("SCC.txt", " ")
    test2.topo_sort()
    dict2 = test2.find_scc()
    len_array2 = []
    for scc in dict2.values():
        len_array2.append(len(scc))
    len_array2.sort(reverse=True)
    print(dict2[1])
    print(dict2[2])
    print(len_array2)
