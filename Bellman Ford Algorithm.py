#Bellman Ford Algorithm.

def edgeAndWeight(graphEdges,edgeWeight):
  '''Combines the edge nodes and weight '''
    edgesWeightList = []
    for i in range(len(graphEdges)):
        node1 = graphEdges[i][0]
        node2 = graphEdges[i][1]
        weight = edgeWeight[i]
        edgesWeightList.append((node1,node2,weight))
    return edgesWeightList

def relaxation(graphLength,edgesWeightList,edgeWeightSum,distance):
  
  '''Realxes the edges as per the algorithm'''
    
    for i in range(graphLength-1):
        for edge in edgesWeightList:
            u = edge[0]
            v = edge[1]
            weight = edge[2]
            if(distance[u] == edgeWeightSum and distance[v] == edgeWeightSum):
                continue
            else:
                if(distance[u]+weight < distance[v]):
                    distance [v] = distance[u]+weight 
        print(distance)
    
    pass

if __name__ == "__main__":
    
    graphLength = 5
    graphEdges = [(3,2),(5,3),(0,1),(1,5),(1,2),(3,4),(2,4)]
    edgeWeight = [6,1,5,-3,-2,-2,3]
    edgeWeightSum = sum(edgeWeight)
    #Step 1
    edgesWeightList = edgeAndWeight(graphEdges,edgeWeight)
    print(edgesWeightList)
    distance = [edgeWeightSum for x in range(graphLength+1)]
    source = 0
    distance[source] = 0
    #Step 2
    relaxation(graphLength,edgesWeightList,edgeWeightSum,distance)
    
    
    
    
