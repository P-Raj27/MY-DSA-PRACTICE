#Check if a graph has cycle or not.

#We will modify the BFS program.

def create_adjacency_list(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    
    return adj_list

def bfs(num,adj_lst):
    #print("hi")
    queue = []
    print(num)
    queue.append((num,-1))
    visited[num] =1
    final_lst =[]
    final_lst.append(num)
    #prev = -1
    #print (queue[0])
    while (len(queue) > 0):
        #print(queue)
        #print (queue[0][0])
        if(len(adj_lst[queue[0][0]]) > 0):
            prev = queue[0][1]
            
            #print("prev is = ", prev)
            for i in adj_lst[queue[0][0]]:
                #print("hi")
                #print("i is = ",i)
                #print("prev is = ",prev)
                if (visited[i] == 1 and i != prev):
                    print("Cycle Found")
                    return "CYCLE FOUND"
                elif(visited[i] == 0):
                    queue.append((i,queue[0][0]))
                    final_lst.append(i)
                    print(i)
                    visited[i] = 1
                    #prev = i
            queue.pop(0)
            
    #for i in final_lst:
        #print(i)

if __name__ == "__main__":
    
    graph_vertices = 11
    graph_edges = [(3,5),(5,6),(5,10),(6,7),(7,8),(8,9),(8,11),(9,10),(1,2),(2,4)]
    #graph_edges = [(1,2),(2,3)]
    visited = [0 for x in range(graph_vertices+1)]
    adj_lst = create_adjacency_list(graph_edges,graph_vertices)
    prev = -1
    print (adj_lst)
    #print(visited)
    for num in range(1,graph_vertices+1):
        
        if(visited[num] == 0):
            
            bfs(num,adj_lst)
    print(visited)
    
