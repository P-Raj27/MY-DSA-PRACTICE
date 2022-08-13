#Bipartite Graphs Y/N
#Using BFS.

def create_adjacency_list(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    
    return adj_list


def bfs_bipartite(num,adj_lst):
    
    queue = []
    queue.append(num)
    visited[num] =0
    #prev_node_color = visited[num]
    #final_lst.append(num)
    while (len(queue) > 0):
        #print(queue)
        prev_node_color = visited[queue[0]]
        if(len(adj_lst[queue[0]]) > 0):
            
            for i in adj_lst[queue[0]]:
                #print("hi")
                
                if(visited[i] == -1):
                    queue.append(i)
                    #final_lst.append(i)
                    if(prev_node_color == 0):
                        visited[i] = 1
                    else:
                        visited[i] = 0
                else:
                    if(visited[i] == prev_node_color):
                        return False
                        #return
                    else:
                        continue
            queue.pop(0)
    return True


if __name__ == "__main__":
    
    graph_vertices = 8
    graph_edges = [(1,2),(2,3),(2,7),(3,4),(4,5),(5,6),(6,7),(5,8)]
    #graph_edges = [(1,2),(2,3),(2,8),(3,4),(8,5),(5,6),(6,7),(4,5)]
    visited = [-1 for x in range(graph_vertices+1)]
    adj_lst = create_adjacency_list(graph_edges,graph_vertices)
    
    print (adj_lst)
    #for num in range(1,graph_vertices+1):
        
     #   if(visited[num] == -1):
            
      #      bfs(num,adj_lst)
    
    bfs(num,adj_lst) 
