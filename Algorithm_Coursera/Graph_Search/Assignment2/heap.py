class Heap(object):

    def __init__(self, init_list):
        self.heap_list = []
        self.len = 0
        self.heapify(init_list)

    def insert(self, item:int):
        self.heap_list.append(item)
        self.len += 1
        self.bubbleUp(self.len-1)

    def bubbleUp(self, pos:int):
        if(pos>0):
            parent = (pos-1)//2
            if self.heap_list[pos] < self.heap_list[parent]:
                self.heap_list[pos], self.heap_list[parent] = self.heap_list[parent], self.heap_list[pos]
                self.bubbleUp(parent)
    
    def bubbleDown(self, pos:int):
        left_child = pos * 2 + 1
        right_child = pos * 2 + 2
        smaller_child = 0

        if right_child <= self.len - 1:
            if self.heap_list[left_child] <= self.heap_list[right_child]:
                smaller_child = left_child
            else:
                smaller_child = right_child
        elif left_child == self.len - 1:
            smaller_child = left_child

        if smaller_child != 0:
            if self.heap_list[pos] > self.heap_list[smaller_child]:
                self.heap_list[pos], self.heap_list[smaller_child] = self.heap_list[smaller_child], self.heap_list[pos]
                self.bubbleDown(smaller_child)
        
    def extractMin(self):
        min = -1
        if self.len != 0:
            min = self.heap_list[0]
            self.heap_list[0] = self.heap_list.pop()
            self.bubbleDown(0)
            self.len -= 1
        return min
    
    def delete(self, pos:int):
        if pos == self.len -1 :
            self.heap_list.pop()
            self.len -= 1
        else:
            self.heap_list[pos], self.heap_list[self.len-1] = self.heap_list[self.len-1], self.heap_list[pos]
            deleted = self.heap_list.pop()
            self.len -= 1
            if self.heap_list[pos] > deleted:
                self.bubbleUp(pos)
            elif self.heap_list[pos] < deleted:
                self.bubbleDown(pos)

    def heapify(self, init_list):
        self.heap_list = []
        for item in init_list:
            self.insert(item)

    def get(self):
        return self.heap_list


if __name__ == "__main__":
    heap = Heap([5,3,4,2,6])
    print(heap.get())
    heap.insert(1)
    print(heap.get())
    heap.delete(3)
    print(heap.get())
    heap.extractMin()
    print(heap.get())