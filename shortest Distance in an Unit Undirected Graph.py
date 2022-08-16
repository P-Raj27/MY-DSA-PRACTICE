#Shortest Path in Undirected Graph and Unweighted Graph using BFS
def create_adjacency_list(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    
    for i in graph:
        
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    
    return adj_list


def shortestDistance(adj_lst,queue):
    
    '''Finds the shortest Distance between of a node from source'''
    
    while(len(queue) > 0):
        
        if(len(adj_lst[queue[0]]) > 0):
            
            for node in adj_lst[queue[0]]:
                
                if((distanceList[queue[0]]+1) < distanceList[node]):
                    #print("here")
                    distanceList[node] = distanceList[queue[0]]+1
                    queue.append(node)
        queue.pop(0)

            
if __name__ == "__main__":
    
    graphLength = 8
    graphEdges = [(0,1),(0,3),(1,3),(1,2),(3,4),(4,5),(2,6),(5,6),(6,7),(7,8),(6,8)]
    #Enter the Source Node from where to Start 
    source_node = 0 
    #Enter the Destination node where you need to reach
    destination_node = 6      
    adj_lst = create_adjacency_list(graphEdges,graphLength)
    
    print(adj_lst)
    
    distanceList = [(graphLength+1) for x in range(graphLength+1) ]
    distanceList[source_node] = 0
    
    #print(distanceList)
    
    queue = [source_node]
    visited = [0 for x in range(graphLength+1)]
    
    shortestDistance(adj_lst,queue) 
    
    #print(distanceList)
    
    print(f"The Distance from Node {source_node} to Node {destination_node} is equal to = {distanceList[destination_node]}")
                    
                
    
    
    


