from maxheap import MaxHeap
from minheap import MinHeap
import math

class Median(object):
    def __init__(self, filename):
        self.H1 = MaxHeap([])
        self.H2 = MinHeap([])
        self.median = []
        self.input_stream = []
        self.load(filename)
        self.feed()

    def load(self, filename):
        file = open(filename, "r") 
        data = file.readlines()
        for line in data:
            self.input_stream.append(int(line))

    def print(self):
        print(self.median)

    def solve(self):
        total = 0
        for i in range(len(self.median)):
            total += self.median[i]
        print(total%10000)

    def feed(self):
        while(len(self.input_stream)>0):
            num = self.input_stream.pop(0)
            h1_max = self.H1.findMax()
            if h1_max is None:
                h1_max = 0
            h2_min = self.H2.findMin()
            if h2_min is None:
                h2_min = math.inf

            if num > h1_max and num < h2_min:
                if self.H1.length() >= self.H2.length():
                    self.H2.insert(num)
                else:
                    self.H1.insert(num)
            else:
                if num < h1_max:
                    self.H1.insert(num)
                elif num > h2_min:
                    self.H2.insert(num)
                
            if self.H1.length() == self.H2.length():
                self.median.append(self.H1.findMax())
            elif self.H1.length() - self.H2.length() == 1:
                self.median.append(self.H1.findMax())
            elif self.H2.length() - self.H1.length() == 1:
                self.median.append(self.H2.findMin())
            elif self.H1.length() - self.H2.length() > 1:
                temp = self.H1.extractMax()
                self.H2.insert(temp)
                self.median.append(self.H1.findMax())
            elif self.H2.length() - self.H1.length() > 1:
                temp = self.H2.extractMin()
                self.H1.insert(temp)
                self.median.append(self.H1.findMax())
            else:
                print("????")

            # print("--------")    
            # print(self.median)
            # print(self.H1.heap_list, self.H2.heap_list)
            

if __name__ == "__main__":
    median = Median("Median.txt")
    #median.print()
    median.solve() # 1213