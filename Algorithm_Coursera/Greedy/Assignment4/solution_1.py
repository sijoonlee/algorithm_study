#knapsack iterative
filename = "knapsack1.txt"
# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]

file = open(filename, "r") 
data = file.readlines()

knapsack_size = int(data[0].split(" ")[0])
num_items = int(data[0].split(" ")[1])

values = [0 for i in range(num_items+1)]
weights = [0 for i in range(num_items+1)]
for i in range(1, num_items+1):
    values[i] = int(data[i].split(" ")[0])
    weights[i] = int(data[i].split(" ")[1])

A = [[0 for n in range(knapsack_size+1)] for i in range(num_items+1)]

# for c in range(knapsack_size+1):
#     A[0][c] = 0

for i in range(1, num_items+1):
    for c in range(knapsack_size+1):
        if weights[i] > c:
            A[i][c] = A[i-1][c]
        else:
            A[i][c] = max(A[i-1][c], A[i-1][c-weights[i]]+values[i])

print(A[num_items][knapsack_size])
