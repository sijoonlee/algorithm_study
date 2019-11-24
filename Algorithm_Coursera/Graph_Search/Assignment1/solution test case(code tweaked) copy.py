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

    # for node in nodes:
    #     if len(gr[node]) == 0 and visited_scc[node] == False: # no heads
    #         stack = []
    #         stack.append(node)
    #         while(stack):
    #             stack_node = stack.pop()
    #             if visited_scc[stack_node] == False:
    #                 visited_scc[stack_node] = True
    #                 visited[stack_node] = True
    #                 scc[sccNo].append(stack_node)
    #                 sccNo += 1
    #                 for tail in r_gr[stack_node]:
    #                     if len(r_gr[tail]) == 0:
    #                         stack.append(tail)
                        

    #     if len(r_gr[node]) == 0 and visited_scc[node] == False: # no tails
    #         stack = []
    #         stack.append(node)
    #         while(stack):
    #             stack_node = stack.pop()
    #             if visited_scc[stack_node] == False:
    #                 visited_scc[stack_node] = True
    #                 visited[stack_node] = True
    #                 scc[sccNo].append(stack_node)
    #                 sccNo += 1
    #                 for head in gr[stack_node]:
    #                     if len(gr[head]) == 0:
    #                         stack.append(head)
    
    for node in nodes:
        if visited[node] == True:
            continue
        stack.append(node)
        found = 0
        while stack:
            stack_node = stack.pop()
            if stack_node == node:
                found += 1
            if visited[stack_node] == False:
                visited[stack_node] = True
                order.append(stack_node)
                for head in r_gr[stack_node]:
                    stack.append(head)
        if found <= 1:  # take out single-node SCC
            visited_scc[node] = True
            scc[sccNo].append(node)
            sccNo += 1
            
    
    ########################################################
    # DFS on original graph
    
    stack = []
    # order = order[1:] # delete node 0 which doesn't exist
    order.reverse()  # The nodes should be visited in reverse finishing times
    for node in order:
        if visited_scc[node] == True:
            continue
        stack.append(node)
        sccNo += 1
        found = 0
        while stack:
            stack_node = stack.pop()
            if stack_node == node:
                found += 1
            if visited_scc[stack_node] == False:
                visited_scc[stack_node] = True
                scc[sccNo].append(stack_node)
                for tail in gr[stack_node]:
                    stack.append(tail)
        if found <= 1 and len(scc[sccNo]) > 1: 
            # take out single-node SCC
            scc[sccNo].remove(node)
            sccNo += 1
            scc[sccNo].append(node)


    # post-adjustment for single-node SCC at the back of the other SCC 
    # too slow

    # scc_list = list(scc.values())
    # for a_scc in scc_list:
    #     if len(a_scc) > 1:
    #         a_scc.reverse()
    #         found = False
    #         to_be_deleted = [None] * len(a_scc)
    #         for i in range(len(a_scc)):
    #             for j in range(len(a_scc)):
    #                 if i is not j:
    #                     if a_scc[j] in gr[a_scc[i]]:
    #                         found = True
    #             if found is False:
    #                 to_be_deleted[i] = a_scc[i]
    #         for i in range(len(a_scc)):
    #             if to_be_deleted[i]:
    #                 scc[len(scc)+1].append(a_scc[i])
    #                 a_scc.remove(a_scc[i])

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
        print("len", len_array[:5])
        print("seed",seed, "total # SCCs",totalScc)


# len [4, 3, 3, 1]
# seed 0 total # SCCs 4
# len [4, 3, 3, 1]
# seed 1 total # SCCs 4
# len [4, 3, 3, 1]
# seed 2 total # SCCs 4
# len [4, 3, 3, 1]
# seed 3 total # SCCs 4
# len [4, 3, 3, 1]
# seed 4 total # SCCs 4
# len [7, 4]
# seed 5 total # SCCs 2
# len [7, 4]
# seed 6 total # SCCs 2
# len [4, 3, 3, 1]
# seed 7 total # SCCs 4
# len [4, 3, 3, 1]
# seed 8 total # SCCs 4
# len [7, 4]
# seed 9 total # SCCs 2