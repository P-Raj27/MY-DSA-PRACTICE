def createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights):
    
    adj_list = [[] for x in range (graphLength+1)]
    k = 0
    for edge in graphEdges:
        adj_list[edge[0]].append((edge[1],edgeWeights[k]))
        adj_list[edge[1]].append((edge[0],edgeWeights[k]))
        #print(edge[0],edge[1])
        k = k+1
    return adj_list
def shortestPathUndirected(adj_lst,distance):
    distance[source] = 0
    q.put((0,source))
    while(len(queue) > 0):
        node = queue[0][1]
        #print("node =",node)
        
        for i in adj_lst[node]:
            weight = i[1]
            if(distance[i[0]] >  distance[node]+weight):
                #print("i of 0 =",i[0])
                distance[i[0]] = distance[node]+weight
                #print(f"distance of {i[0]} =",distance[node]+weight)
                q.put((distance[i[0]],i[0]))
        q.get()
    print(distance)
    return distance
                
               
    
    


if __name__ == "__main__":
    graphLength = 5
    graphEdges = [(1,2),(2,5),(2,3),(4,3),(1,4),(3,5)]
    edgeWeights = [2,5,4,3,1,1]
    edgeWeightsSum = sum(edgeWeights)
    adj_lst = createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights)
    print(adj_lst)
    distance = [edgeWeightsSum for x in range(graphLength+1)]
    source = 4
    shortestPathUndirected(adj_lst,distance)
    print(distance[5])
    
    
    
    
    
    
