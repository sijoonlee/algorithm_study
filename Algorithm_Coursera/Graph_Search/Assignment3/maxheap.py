class MaxHeap(object):

    def __init__(self, init_list):
        self.heap_list = []
        self.heapify(init_list)
    
    def length(self):
        return len(self.heap_list)
    
    def findMax(self):
        max = None
        if(len(self.heap_list)>0):
            max = self.heap_list[0]
        return max

    def insert(self, item:int):
        self.heap_list.append(item)
        self.bubbleUp(len(self.heap_list)-1)

    def bubbleUp(self, pos:int):
        if(pos>0):
            parent = (pos-1)//2
            if self.heap_list[pos] > self.heap_list[parent]:
                self.heap_list[pos], self.heap_list[parent] = self.heap_list[parent], self.heap_list[pos]
                self.bubbleUp(parent)
    
    def bubbleDown(self, pos:int):
        left_child = pos * 2 + 1
        right_child = pos * 2 + 2
        larger_child = 0

        if right_child <= len(self.heap_list) - 1:
            if self.heap_list[left_child] >= self.heap_list[right_child]:
                larger_child = left_child
            else:
                larger_child = right_child
        elif left_child == len(self.heap_list) - 1:
            larger_child = left_child

        if larger_child != 0:
            if self.heap_list[pos] < self.heap_list[larger_child]:
                self.heap_list[pos], self.heap_list[larger_child] = self.heap_list[larger_child], self.heap_list[pos]
                self.bubbleDown(larger_child)
        
    def extractMax(self):
        max = None
        if len(self.heap_list) != 0:
            max = self.heap_list[0]
            self.heap_list[0] = self.heap_list.pop()
            self.bubbleDown(0)
        return max
    
    def delete(self, pos:int):
        if pos == len(self.heap_list) -1 :
            self.heap_list.pop()
        else:
            self.heap_list[pos], self.heap_list[len(self.heap_list)-1] = self.heap_list[len(self.heap_list)-1], self.heap_list[pos]
            deleted = self.heap_list.pop()
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
    heap = MaxHeap([5,3,4,2,6])
    print(heap.get())
    heap.insert(1)
    print(heap.get())
    heap.delete(3)
    print(heap.get())
    heap.extractMax()
    print(heap.get())
