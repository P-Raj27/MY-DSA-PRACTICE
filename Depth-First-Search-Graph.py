#DFS for Graph

def dfs(num,adj_lst):
    
    visited[num] = 1
    
    if(len(adj_lst[num]) != 0):
        for i in adj_lst[num]:
            if(visited[i] == 0):
                dfs(i,adj_lst)
                
def create_adjacency_list(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    
    return adj_list

if __name__ == "__main__":
    
    graph_vertices = 7
    graph_edges = [(1,2),(2,3),(2,7),(3,5),(4,6),(5,7)]
    visited = [0 for x in range(graph_vertices+1)]
    adj_lst = create_adjacency_list(graph_edges,graph_vertices)
    
    print (adj_lst)
    for num in range(1,graph_vertices+1):
        
        if(visited[num] == 0):
            
            dfs(num,adj_lst)
            #finalLst.append() 
