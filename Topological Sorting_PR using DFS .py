#Topological Sorting using DFS (Stack is the key data structure used.)


def create_adjacency_list_directed(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        #adj_list[i[1]].append(i[0])
    
    return adj_list


def dfs(num,adj_lst,stack):
    
    visited[num] = 1
    
    if(len(adj_lst[num]) != 0):
        for i in adj_lst[num]:
            if(visited[i] == 0):
                dfs(i,adj_lst,stack)
                stack.append(i)
            
if __name__ == "__main__":
    
    graphLength = 5
    graphEdges = [(5,0),(4,0),(5,2),(2,3),(3,1),(4,1)]
    
    adj_lst = create_adjacency_list_directed(graphEdges,graphLength)
    visited = [0 for x in range(graphLength+1)]
    print(adj_lst)
    stack = []
    for num in range(0,graphLength+1):
        if (visited[num] == 0):
            dfs(num,adj_lst,stack)
            stack.append(num)
    print(stack[::-1])
    

