# Huffman

import heapq

from collections import defaultdict

class Tree(object):
    def __init__(self, left=None, right=None):
        self.id = None
        self.child = defaultdict(list)
        if left!= None and right != None:
            self.weight = left.weight + right.weight
            for id in left.id:
                self.child[id] = left.child[id]
                self.child[id].insert(0,0)
            for id in right.id:
                self.child[id] = right.child[id]
                self.child[id].insert(0,1)
        elif left!= None and right == None:
            self.weight = left.weight
            for id in left.id:
                self.child[id] = left.child[id]
                self.child[id].insert(0,0)
        elif left == None and right == None:
            self.weight = 0       
        self.left = left
        self.right = right
        self.id = list(self.child.keys())

    def __lt__(self, other):
        if other == None:
            return False
        elif self.weight < other.weight:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if other == None:
            return False
        elif self.weight == other.weight:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if other == None:
            return False
        elif self.weight > other.weight:
            return True
        else:
            return False
    
class Huffman(object):
    def __init__(self, filename):

        file = open(filename, "r") 
        data = file.readlines()
        self.num_nodes = int(data[0])
        self.trees = []
        for i in range(1, len(data)):
            t = Tree(None, None)
            t.id = [i]
            t.weight = int(data[i])
            self.trees.append(t)

        heapq.heapify(self.trees)

        while len(self.trees) > 2:
            t1 = heapq.heappop(self.trees)
            t2 = heapq.heappop(self.trees)
            t3 = Tree(t1, t2)
            heapq.heappush(self.trees, t3)




if __name__=="__main__":
    h = Huffman("huffman.txt")
    #print(h.trees[0].child)
    #print(h.trees[1].child)

    left = list(h.trees[0].child.values())
    sorted_idx = sorted(range(len(left)), key = lambda k: len(left[k]))
    print(len(left[sorted_idx[0]])+1)
    print(len(left[sorted_idx[-1]])+1)

    right = list(h.trees[1].child.values())
    sorted_idx = sorted(range(len(right)), key = lambda k: len(right[k]))
    print(len(right[sorted_idx[0]])+1)
    print(len(right[sorted_idx[-1]])+1)

# 9
# 16
# 9
# 19