def scc_finder(seedNo):
    # Copyright David Bai: Anyone can use this code without permission or referencing the original source
    """
    W1 Kosaraju Algorithm
    List Based Iterative Implementation to find sizes of strongly connected components
    """
    ########################################################
    # Data Structures
    num_nodes = 875716

    # Adjacency representations of the graph and reverse graph
    gr = [[] for i in range(num_nodes)]
    r_gr = [[] for i in range(num_nodes)]

    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * num_nodes

    # The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
    # scc = [0] * num_nodes
    from collections import defaultdict
    scc = defaultdict(list)

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
    visited[0] = True # prevent using node 0 which doesn't exist

    import random
    nodes = [i for i in range(num_nodes)]

    random.seed(seedNo) 
    ##################################################### change seed and try

    random.shuffle(nodes)

    for node in nodes:
        if visited[node] == True:
            continue
        stack.append(node)
        while stack:
            stack_node = stack.pop()
            if visited[stack_node] == False:
                visited[stack_node] = True
                order.append(stack_node)
                for head in r_gr[stack_node]:
                    stack.append(head)
    
    # print(order)
    ########################################################
    # DFS on original graph

    visited = [False] * num_nodes  # Resetting the visited variable
    stack = []
    # order = order[1:] # delete node 0 which doesn't exist
    order.reverse()  # The nodes should be visited in reverse finishing times
    sccNo = 0

    # for node in order:
    #     if len(gr[node]) == 0:
    #         visited[node] = True
    #         sccNo += 1
    #         scc[sccNo].append(node)

    for node in order:
        if visited[node] == True:
            continue
        stack.append(node)
        sccNo += 1
        while stack:
            stack_node = stack.pop()
            if visited[stack_node] == False:
                visited[stack_node] = True
                scc[sccNo].append(stack_node)
                for tail in gr[stack_node]:
                    if visited[tail] == False:
                        stack.append(tail)
       

    # ########################################################
    # # return scc
    return scc



if __name__ == "__main__":
    totalScc = 0
    seed_list = []
    scc_list = [0] * 10
    the_len_array = []
    for seed in range(10):
        scc = scc_finder(seed)
        len_array = []
        for arr in scc.values():
            len_array.append(len(arr))
        if(totalScc < len(len_array)):
            totalScc = len(len_array)
            seed_list.append(seed)
            scc_list[seed] = scc
            len_array.sort(reverse=True)
            the_len_array = len_array
            print(the_len_array[:5])
            print(seed, totalScc)
# [434821, 969, 459, 313, 211]
# 0 340864
# [434821, 1179, 459, 313, 205]
# 3 341031