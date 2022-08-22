#Prim's Algorithm for minimun spanning tree of Graph.

def createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights):
    
    adj_list = [[] for x in range (graphLength+1)]
    k = 0
    for edge in graphEdges:
        adj_list[edge[0]].append((edge[1],edgeWeights[k]))
        adj_list[edge[1]].append((edge[0],edgeWeights[k]))
        #print(edge[0],edge[1])
        k = k+1
    return adj_list


def prims():
    key = []
    mst = []
    parent = []
    for i in range(graphLength+1):
        key.append(edgeWeightsSum+1)
        mst.append(False)
        parent.append(-1)
    key[0] = 0
    parent[0] = -1
    currNode = 0
    while (all(mst) == False):
        #print("I am inside the while loop")
        mst[currNode] = True
        for adj in adj_lst[currNode]:
            node = adj[0]
            weight = adj[1]
            if(mst[node] == False and weight < key[node]):
                key[node] = weight
                parent[node] = currNode
        minimum = edgeWeightsSum+1
        index = 0
        print(key)
        for i in range(len(key)):
            if(key[i]<minimum and mst[i] == False):
                minimum = key[i]
                
                index = i
                
        currNode = index
        print("Minium is =",minimum)
        print(mst,"current node is",currNode)
    print("key is ",key)
    print("parent is ",parent)
    print("current Node ",currNode)
    
            
            
            
            
            
            
        
        
    
if __name__ == "__main__":
    
    graphLength = 4
    graphEdges = [(0,1),(0,3),(1,3),(1,2),(1,4),(4,2)]
    edgeWeights = [2,6,8,3,5,7]
    edgeWeightsSum = sum(edgeWeights)
    
    adj_lst = createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights)
    print(adj_lst)
    prims()
    
    
