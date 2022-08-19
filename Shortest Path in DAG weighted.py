# Shortest Path in DAG Weighted.

def createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights):
    
    adj_list = [[] for x in range (graphLength+1)]
    k = 0
    for edge in graphEdges:
        adj_list[edge[0]].append((edge[1],edgeWeights[k]))
        #print(edge[0],edge[1])
        k = k+1
    return adj_list

def create_adjacency_list_directed(graph , len_graph):
    """Creating adjacentcy list of the Graph Input"""
    
    adj_list = [[] for x in range (len_graph+1)]
    for i in graph:
        adj_list[i[0]].append(i[1])
        #adj_list[i[1]].append(i[0])
    return adj_list


def dfs(num,adj_lst,stack):
    
    visited[num] = 1
    if(len(adj_lst[num]) != 0):
        for i in adj_lst[num]:
            if(visited[i] == 0):
                dfs(i,adj_lst,stack)
                stack.append(i)
                
def shortedDistance(topologicalSorted,distance,adj_lst,source):
    flag = 0
    while (len(topologicalSorted) > 0):
        if(distance[topologicalSorted[0]] != edgeWeightsSum):
            for edge in adj_lst[topologicalSorted[0]]:
                node = edge[0]
                weight = edge[1]
                if(distance[node] > distance[topologicalSorted[0]]+weight):
                    distance[node] = distance[topologicalSorted[0]]+weight
        topologicalSorted.pop(0)
    return(distance)
def nodesCanVisited(distance):
    lst = []
    for i in range(len(distance)):
        if(distance[i] < edgeWeightsSum):
            lst.append(i)
    return lst
if __name__ == "__main__":
    
    graphLength = 5
    graphEdges = [(0,1),(0,4),(1,2),(2,3),(4,2),(4,5),(5,3)]
    edgeWeights = [2,1,3,6,2,4,1]
    edgeWeightsSum = sum(edgeWeights)
    adj_lst = createDirectedAdjacencyListWeighted(graphEdges,graphLength,edgeWeights)
    
    #Find the topological sorting.
    
    adj_lst1 = create_adjacency_list_directed(graphEdges,graphLength)
    visited = [0 for x in range(graphLength+1)]
    stack = []
    for num in range(0,graphLength+1):
        if (visited[num] == 0):
            dfs(num,adj_lst1,stack)
            stack.append(num)
    topologicalSorted = stack[::-1]
    
    #Finding the shortest distance to each nodes.
    
    source = int(input("Please Enter the Source of your Journey = "))
    distance = [edgeWeightsSum for x in range(graphLength+1)]
    distance[source] = 0
    distance = shortedDistance(topologicalSorted,distance,adj_lst,source)
    #nodesCanbeVisited = nodesCanVisited(distance)
    nodesCanBeVisited = nodesCanVisited(distance)
    destination = int(input(f"Enter the destination from the following nodes {nodesCanBeVisited} = "))
    if(distance[destination] == edgeWeightsSum):
        print("Sorry Node not reachable from here")
    elif(distance[destination] == 0):
        print("Dude! You are already at that Node")
    else:
        print(distance[destination])
