#KosaRaju's Algorithm

def create_adjacency_list_directed(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        #adj_list[i[1]].append(i[0])
    
    return adj_list

def transpose(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[1]].append(i[0])
        #adj_list[i[1]].append(i[0])
    
    return adj_list


def dfs(num,adj_lst,stack):
    
    visited[num] = 1
    
    if(len(adj_lst[num]) != 0):
        for i in adj_lst[num]:
            if(visited[i] == 0):
                dfs(i,adj_lst,stack)
                stack.append(i)
def revDfs(num,transpose):
    
    visited2[num] = 1
    print(num,end ="")
    if(len(transpose[num]) != 0):
        for i in transpose[num]:
            if(visited2[i] == 0):
                revDfs(i,transpose)
                #stack.append(i)
                
                
if __name__ == "__main__":
    
    graphEdges = [(1,2),(2,3),(3,1),(4,5),(2,4)]
    graphLength = 5
    
    #Step1 - Sort the given graph in Topological sort.
    
    adj_lst = create_adjacency_list_directed(graphEdges,graphLength)
    visited = [0 for x in range(graphLength+1)]
    print(adj_lst)
    stack = []
    for num in range(1,graphLength+1):
        if (visited[num] == 0):
            dfs(num,adj_lst,stack)
            stack.append(num)
    print(stack[::-1])
    toposort = stack[::-1]
    
    #Step 2 - Transpose the graph (Reverse the direction of each edge)
    
    transpose = transpose(graphEdges,graphLength)
    print(transpose)
    
    #Step 3 - Performing DfS Again according to the Topological Sort Stack.
    
    visited2 = [0 for x in range(graphLength+1)]
    for i in toposort:
       # toposort.pop(0);
        if(visited2[i] == 0):
            print()
            print("Scc: ",end = "")
            revDfs(i,transpose)
        #toposort.pop(0);
        
        
        
    
    
    
    
