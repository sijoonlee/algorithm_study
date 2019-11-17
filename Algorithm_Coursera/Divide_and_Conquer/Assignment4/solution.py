
import random

class Solution(object):

    def __init__(self, file, sep):
        arr = []

        with open(file, 'r') as f:
            for str in f:
                line = [int(s)-1 for s in str.rstrip().split(sep)]
                arr.append(line[1:])

        self.edges = []
        self.vertexes = [i for i in range(len(arr))]
        for i, row in enumerate(arr):
            for item in row:
                self.edges.append([i, item])
                arr[item].remove(i)


    def choose_randomly(self):

        idx = random.randint(0, len(self.edges) - 1)
        x = self.edges.pop(idx)
        return x

    def merge_vertexes(self, chosen_edge):

        delete = []

        for idx in range(len(self.edges)):
            if self.edges[idx][0] == chosen_edge[1] :
                self.edges[idx][0] = chosen_edge[0]
            if self.edges[idx][1] == chosen_edge[1] :
                self.edges[idx][1] = chosen_edge[0]
            if self.edges[idx][0] == self.edges[idx][1]:
                delete.append(idx)

        delete.reverse()
        for idx in delete:
            self.edges.pop(idx)

    def contract(self):
        while(len(self.vertexes) > 2):
            chosen_edge = self.choose_randomly()
            self.vertexes.remove(chosen_edge[1])
            self.merge_vertexes(chosen_edge)


    def report(self):
        #print("Graph is contracted into", self.vertexes)
        #print("# Edges in the cut", len(self.edges))
        return len(self.edges)

if __name__ == "__main__":

    # test = Solution("test.txt", ' ')
    # test.contract()
    # test.report()

    min = 30
    for i in range(100):
        test2 = Solution("kargerMinCut.txt", '\t')

        test2.contract()
        cuts = test2.report()

        if cuts<min :
            min = cuts
    print(min) # 17
