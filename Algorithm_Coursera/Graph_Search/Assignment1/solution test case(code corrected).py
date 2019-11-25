import math

def scc_finder(seedNo):
    # Copyright David Bai: Anyone can use this code without permission or referencing the original source
    """
    W1 Kosaraju Algorithm
    List Based Iterative Implementation to find sizes of strongly connected components
    """
    ########################################################
    # Data Structures
    num_nodes = 12 # node range from 1 to 875715

    # Adjacency representations of the graph and reverse graph
    gr = [[] for i in range(num_nodes)]
    r_gr = [[] for i in range(num_nodes)]

    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * num_nodes
    visited[0] = True # prevent using node 0 which doesn't exist

    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.

    visited_scc = [False] * num_nodes  # Resetting the visited variable

    from collections import defaultdict
    scc = defaultdict(list)
    sccNo = 0


    stack = []  # Stack for DFS
    order = []  # The finishing orders after the first pass
    
    ########################################################
    # Importing the graphs
    file = open("test1.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
    data = file.readlines()

    # node labels range from 1 to 875714
    for line in data:
        items = line.split()
        gr[int(items[0])] += [int(items[1])]
        r_gr[int(items[1])] += [int(items[0])]

    # ########################################################
    # # DFS on reverse graph

    import random
    nodes = [i for i in range(num_nodes)]
    random.seed(seedNo)  # change seed and try
    random.shuffle(nodes) 
   
    print("node order in 1st DFS", nodes)
    for node in nodes:
        if visited[node] == True:
            continue
        stack.append(node)
        visited[node] = True

        stack_node = -math.inf

        while stack:
            print(stack_node, stack[-1])
            
            if stack_node == stack[-1]:
            
                stack.pop()
                order.append(stack_node)
            
            else:
                stack_node = stack[-1]
                
                for head in r_gr[stack_node]:
                    if visited[head] == False:
                        visited[head] = True
                        stack.append(head)


    
    ########################################################
    # DFS on original graph
    
    stack = []
    # order = order[1:] # delete node 0 which doesn't exist
    order.reverse()  # The nodes should be visited in reverse finishing times
    print("order in 2nd DFS", order)
    for node in order:
        if visited_scc[node] == True:
            continue
        stack.append(node)
        visited_scc[node] = True
        sccNo += 1
        stack_node = -math.inf
        while stack:
            if stack_node == stack[-1]:
                scc[sccNo].append(stack_node)
                stack.pop()
            else:
                stack_node = stack[-1]
                for tail in gr[stack_node]:
                    if visited_scc[tail] == False:
                        visited_scc[tail] = True
                        stack.append(tail)
    # # return scc
    return scc



if __name__ == "__main__":
    trials = 10
    totalScc = 0
    for seed in range(trials):
        scc = scc_finder(seed)
        len_array = []
        for arr in scc.values():
            len_array.append(len(arr))
        totalScc = len(len_array)
        len_array.sort(reverse=True)
        
        print("scc", scc)
        print("len", len_array[:5])
        print("seed",seed, "total # SCCs",totalScc)
        print("####################################")


# node order in 1st DFS [1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6]
# order in 2nd DFS [6, 10, 11, 8, 2, 4, 7, 9, 3, 5, 1]
# scc defaultdict(<class 'list'>, {1: [6, 10, 8], 2: [11], 3: [2, 4, 7, 9], 4: [3, 5, 1]})
# len [4, 3, 3, 1]
# seed 0 total # SCCs 4
# ####################################
# node order in 1st DFS [7, 11, 0, 8, 5, 6, 3, 10, 4, 1, 9, 2]
# order in 2nd DFS [6, 10, 8, 11, 2, 9, 4, 1, 3, 5, 7]
# scc defaultdict(<class 'list'>, {0: [11], 2: [6, 10, 8], 3: [2, 4, 7, 9], 4: [1, 3, 5]})
# len [4, 3, 3, 1]
# seed 1 total # SCCs 4
# ####################################
# node order in 1st DFS [9, 11, 3, 4, 7, 6, 8, 2, 5, 10, 1, 0]
# order in 2nd DFS [10, 8, 6, 11, 2, 4, 1, 3, 5, 7, 9]
# scc defaultdict(<class 'list'>, {0: [11], 2: [10, 8, 6], 3: [2, 4, 7, 9], 4: [1, 3, 5]})
# len [4, 3, 3, 1]
# seed 2 total # SCCs 4
# ####################################
# node order in 1st DFS [1, 7, 10, 0, 6, 11, 4, 5, 2, 8, 9, 3]
# order in 2nd DFS [8, 11, 6, 10, 2, 9, 4, 7, 3, 5, 1]
# scc defaultdict(<class 'list'>, {1: [8, 6, 10], 2: [11], 3: [2, 4, 7, 9], 4: [3, 5, 1]})
# len [4, 3, 3, 1]
# seed 3 total # SCCs 4
# ####################################
# node order in 1st DFS [11, 2, 8, 10, 5, 0, 9, 7, 6, 1, 4, 3]
# order in 2nd DFS [6, 10, 8, 4, 7, 9, 2, 5, 1, 3, 11]
# scc defaultdict(<class 'list'>, {0: [11], 2: [6, 10, 8], 3: [4, 7, 9, 2], 4: [5, 1, 3]})
# len [4, 3, 3, 1]
# seed 4 total # SCCs 4
# ####################################
# node order in 1st DFS [10, 2, 11, 7, 1, 3, 6, 0, 8, 5, 4, 9]
# order in 2nd DFS [2, 4, 7, 9, 8, 5, 1, 3, 11, 6, 10]
# scc defaultdict(<class 'list'>, {1: [2, 10, 8, 6, 4, 7, 9], 2: [5, 1, 3, 11]})
# len [7, 4]
# seed 5 total # SCCs 2
# ####################################
# node order in 1st DFS [6, 5, 2, 3, 8, 10, 11, 0, 4, 7, 1, 9]
# order in 2nd DFS [4, 7, 9, 2, 10, 8, 5, 1, 3, 11, 6]
# scc defaultdict(<class 'list'>, {1: [4, 7, 9, 8, 6, 10, 2], 2: [5, 1, 3, 11]})
# len [7, 4]
# seed 6 total # SCCs 2
# ####################################
# node order in 1st DFS [7, 11, 3, 10, 8, 4, 9, 1, 0, 6, 2, 5]
# order in 2nd DFS [8, 6, 10, 11, 2, 9, 4, 1, 3, 5, 7]
# scc defaultdict(<class 'list'>, {0: [11], 2: [8, 6, 10], 3: [2, 4, 7, 9], 4: [1, 3, 5]})
# len [4, 3, 3, 1]
# seed 7 total # SCCs 4
# ####################################
# node order in 1st DFS [7, 8, 4, 1, 9, 0, 10, 11, 2, 6, 5, 3]
# order in 2nd DFS [6, 10, 11, 8, 2, 9, 4, 1, 3, 5, 7]
# scc defaultdict(<class 'list'>, {1: [6, 10, 8], 2: [11], 3: [2, 4, 7, 9], 4: [1, 3, 5]})
# len [4, 3, 3, 1]
# seed 8 total # SCCs 4
# ####################################
# node order in 1st DFS [8, 6, 3, 11, 0, 10, 1, 2, 4, 5, 9, 7]
# order in 2nd DFS [4, 7, 9, 2, 6, 10, 5, 1, 3, 11, 8]
# scc defaultdict(<class 'list'>, {1: [4, 7, 9, 8, 6, 10, 2], 2: [5, 1, 3, 11]})
# len [7, 4]
# seed 9 total # SCCs 2
# ####################################