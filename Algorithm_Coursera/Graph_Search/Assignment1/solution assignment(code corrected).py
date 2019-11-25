import math

def scc_finder(seedNo):
    # Copyright David Bai: Anyone can use this code without permission or referencing the original source
    """
    W1 Kosaraju Algorithm
    List Based Iterative Implementation to find sizes of strongly connected components
    """
    ########################################################
    # Data Structures
    num_nodes = 875716 # node range from 1 to 875715

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
    file = open("SCC.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
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
   
    #print("node order in 1st DFS", nodes)
    for node in nodes:
        if visited[node] == True:
            continue
        stack.append(node)
        visited[node] = True

        stack_node = -math.inf

        while stack:
           
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
    order.reverse()  # The nodes should be visited in reverse finishing times
    # print("order in 2nd DFS", order)
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
        
        # print("scc", scc)
        print("len", len_array[:5])
        print("seed",seed, "total # SCCs",totalScc)
        print("####################################")


# seed 0 total # SCCs 359601
# seed 1 total # SCCs 359103
# seed 2 total # SCCs 359340
# seed 3 total # SCCs 359301
# seed 4 total # SCCs 359415
# seed 5 total # SCCs 359405
# seed 6 total # SCCs 359150
# seed 7 total # SCCs 359081
# seed 8 total # SCCs 358936
# seed 9 total # SCCs 359026