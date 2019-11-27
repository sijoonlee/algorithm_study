import math

class Heap(object):

    def __init__(self, key_list):
        self.idx_list = [i for i in range(1, len(key_list))]
        self.key = key_list

    def length(self):
        return len(self.idx_list)

    def update_key(self, idx, val):
        self.key[idx] = val

    def insert(self, index:int, key_value:int):
        self.idx_list.append(index)
        self.key[index] = key_value
        self.bubbleUp(len(self.idx_list)-1)

    def bubbleUp(self, pos:int):
        if(pos>0):
            parent = (pos-1)//2
            if self.key[self.idx_list[pos]] < self.key[self.idx_list[parent]]:
                self.idx_list[pos], self.idx_list[parent] = self.idx_list[parent], self.idx_list[pos]
                self.bubbleUp(parent)
    
    def bubbleDown(self, pos:int):
        left_child = pos * 2 + 1
        right_child = pos * 2 + 2
        smaller_child = 0

        if right_child <= len(self.idx_list) - 1:
            if self.key[self.idx_list[left_child]] <= self.key[self.idx_list[right_child]]:
                smaller_child = left_child
            else:
                smaller_child = right_child
        elif left_child == len(self.idx_list) - 1:
            smaller_child = left_child

        if smaller_child != 0:
            if self.key[self.idx_list[pos]] > self.key[self.idx_list[smaller_child]]:
                self.idx_list[pos], self.idx_list[smaller_child] = self.idx_list[smaller_child], self.idx_list[pos]
                self.bubbleDown(smaller_child)
        
    def extractMin(self):
        min = -1
        key = -1
        if len(self.idx_list) > 1:
            min = self.idx_list[0]
            key = self.key[self.idx_list[0]]
            self.idx_list[0] = self.idx_list.pop()
            self.bubbleDown(0)
            self.update_key(min, -1)
        elif len(self.idx_list) == 1:
            key = self.key[self.idx_list[0]]
            min = self.idx_list.pop()
            self.update_key(min, -1)
        return min, key
    
    def delete(self, pos:int):
        if pos == len(self.idx_list) -1 :
            idx = self.idx_list.pop()
            self.update_key(idx, -1)
        else:
            self.idx_list[pos], self.idx_list[len(self.idx_list)-1] = self.idx_list[len(self.idx_list)-1], self.idx_list[pos]
            deleted = self.idx_list.pop()
            self.update_key(deleted, -1)
            if self.key[self.idx_list[pos]] > self.key[deleted]:
                self.bubbleUp(pos)
            elif self.key[self.idx_list[pos]] < self.key[deleted]:
                self.bubbleDown(pos)

    def get(self):
        return self.idx_list

    def find(self, label):
        for index in range(len(self.idx_list)):
            if self.idx_list[index] == label:
                break
        if index == len(self.idx_list):
            index = -1
        return index

    def set_start(self, label):
        index = self.find(label)
        self.key[self.idx_list[index]] = 0
    
    def get_key(self, idx):
        return self.key[idx]

    def does_exist(self, idx):
        return self.get_key(idx) >= 0

    

class Dijkstra(object):

    def __init__(self, filename, size):
        self.matrix, self.lookup_tail = self.load(filename, size) # matrix[head_idx][tail_idx] = length between head and tail
        self.size = size

    def load(self, filename, size):
        file = open(filename, "r") 
        data = file.readlines()
        
        lookup_tail = [0] * size
        matrix = [[-1 for x in range(size)] for y in range(size)]
        for line in data:
            items = line.split()
            lookup_row = []
            for item in items[1:]:
                tail_length = item.split(",")
                lookup_row.append(int(tail_length[0]))
                # print(int(items[0]),int(tail_length[0]),int(tail_length[1]))
                matrix[int(items[0])][int(tail_length[0])] = int(tail_length[1])
                # print(matrix)
            lookup_tail[int(items[0])] = lookup_row
        return matrix, lookup_tail
    
    def run(self, start):
        expl = []
        key_list = [math.inf for i in range(self.size)]
        distance_list = [0 for i in range(self.size)]
        unexpl = Heap(key_list)
        unexpl.set_start(start)
        
        while unexpl.length()>0:
            min_idx, dijkstra_score = unexpl.extractMin()
            expl.append(min_idx)
            head = min_idx
            distance_list[head] = dijkstra_score
            if self.lookup_tail[head] != 0:
                for tail in self.lookup_tail[head]:
                    if unexpl.does_exist(tail):
                        a_distance = self.matrix[head][tail]
                        old_key = unexpl.get_key(tail)
                        new_key = min(old_key, dijkstra_score + a_distance)
                        pos = unexpl.find(tail)
                        unexpl.delete(pos)
                        unexpl.insert(tail, new_key)
        return expl, distance_list





if __name__ == "__main__":
    sol = Dijkstra("dijkstraData.txt",201) # total # vertices + 1 since index starts from 1
    expl, distance = sol.run(1)
    # print(expl)
    # 7,37,59,82,99,115,133,165,188,197
    print(distance[7],distance[37],distance[59],distance[82],distance[99],distance[115],distance[133],distance[165], distance[188],distance[197])
    # 2599 2610 2947 2052 2367 2399 2029 2442 2505 3068
    