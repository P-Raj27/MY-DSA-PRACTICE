def create_adjacency_list(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    
    return adj_list


def bfs(num,adj_lst):
    
    queue = []
    queue.append(num)
    visited[num] =1
    final_lst =[]
    final_lst.append(num)
    while (len(queue) > 0):
        #print(queue)
        if(len(adj_lst[queue[0]]) > 0):
            for i in adj_lst[queue[0]]:
                #print("hi")
                if(visited[i] == 0):
                    queue.append(i)
                    final_lst.append(i)
                    visited[i] = 1
            queue.pop(0)
            
    for i in final_lst:
        print(i)
            
if __name__ == "__main__":
    
    graph_vertices = 7
    graph_edges = [(1,2),(2,3),(2,7),(3,5),(4,6),(5,7)]
    visited = [0 for x in range(graph_vertices+1)]
    adj_lst = create_adjacency_list(graph_edges,graph_vertices)
    
    print (adj_lst)
    for num in range(1,graph_vertices+1):
        
        if(visited[num] == 0):
            
            bfs(num,adj_lst)
            #finalLst.append()
