# knapsack recursive

import sys
sys.setrecursionlimit(5000)

filename = "knapsack_big.txt"
# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]


file = open(filename, "r") 
data = file.readlines()

knapsack_size = int(data[0].split(" ")[0])
num_items = int(data[0].split(" ")[1])

values = [0]
weights = [0]
A = {}

for line in data[1:]:
    line = line.split(" ")
    values.append(int(line[0]))
    weights.append(int(line[1]))

for c in range(knapsack_size+1):
    A[(0, c)] = 0

def knapsack(no, size):

    found = A.get((no, size))
    if found != None:
        #print(no, size)
        return found

    if weights[no] > size:
        return knapsack(no-1, size)
    else:
        m = max(knapsack(no-1, size), knapsack(no-1, size-weights[no]) + values[no])
        A[(no, size)] = m
        return m

print(knapsack(num_items, knapsack_size))