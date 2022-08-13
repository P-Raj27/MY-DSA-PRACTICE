def create_adjacency_list_directed(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        #adj_list[i[1]].append(i[0])
    
    return adj_list


def dfs(num,adj_lst,dfsVisited):
    
    visited[num] = 1
    dfsVisited[num] = 1 
    #print("dfs visit is =",dfsVisited,"when num = ",num)
    #print("len of adj = ",len(adj_lst[num]),"when num = ",num)
    if(len(adj_lst[num]) != 0):
        for i in adj_lst[num]:
            if(visited[i] == 0):
                if(dfs(i,adj_lst,dfsVisited)):
                    return True
                
                
            elif(dfsVisited[i] == 1):
                #print("Cyclic",i)
                #print("Code is here")
                return True
    dfsVisited[num] = 0
    return False
         
            #if(visited[i] == 1)

if __name__ == "__main__":
    
    graphEdges = [(1,2),(2,3),(3,4),(3,6),(6,5),(4,5),(7,2),(7,8),(8,9),(9,7)]    #Input for Cyclic Graph
    graphEdges = [(1,2),(2,3)]         #Input for non Cyclic Graph
    graphLength = 9
    adj_lst = create_adjacency_list_directed(graphEdges , graphLength)
    
    visited = [0 for x in range(graphLength+1)]
    dfsVisited = [0 for x in range(graphLength+1)]
    
    print(adj_lst)
    flag = 0
    
    for num in range(1,graphLength+1):
        
        if(visited[num] == 0):
            
            test = dfs(num,adj_lst,dfsVisited)
            #print("test = ",test)
            dfsVisited[num] = 0
            if(test == True):
                flag = 1
                print(f"Cyclic Starting from {num}")
                break
    if(flag == 0):
        print("Sorry! This graph is not cyclic")
        
            #finalLst.append()
    
