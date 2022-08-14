#Topological Sorting using BFS.(Kahn's Algorithm)


def inDegree(graphEdges,graphLength):
    inDegree = [0 for x in range(graphLength+1)]
    for tup in graphEdges:
        
        inDegree[tup[1]] = inDegree[tup[1]] + 1
    return inDegree

def create_adjacency_list_directed(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        #adj_list[i[1]].append(i[0])
    
    return adj_list

def bfs(num,adj_lst,inDegree,queue):
    
    #print(num)
    #queue.pop(0)
    
    while (len(queue) > 0):
        #print(queue)
        #print(queue[0])
        #print("Hi I am here!",queue)
        if(len(adj_lst[queue[0]]) > 0):
            for i in adj_lst[queue[0]]:
                #print("hi")
                if(inDegree[i] ==  0 or inDegree[i] == 1):
                    queue.append(i)
                    #final_lst.append(i)
                    #visited[i] = 1
                else:
                    inDegree[i] = inDegree[i] - 1
        print(queue[0])
        queue.pop(0)
            
    

if __name__ == "__main__":
    
    graphLength = 5
    graphEdges = [(5,0),(4,0),(5,2),(2,3),(3,1),(4,1)]
    
    inDegree = inDegree(graphEdges,graphLength)
    print(inDegree)
    
    adj_lst = create_adjacency_list_directed(graphEdges,graphLength)
    
    print (adj_lst)
    
    queue = []
    for number in range(len(inDegree)):
        if(inDegree[number] == 0):
            queue.append(number)
    
    while(len(queue) > 0):
        
        
        bfs(queue[0],adj_lst,inDegree,queue)
        
        
        
    
    
    
    
    
    
        
