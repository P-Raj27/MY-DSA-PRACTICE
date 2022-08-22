#Kruskal's Algorithm
#Uses Disjoint Data Structure

def findParent(node):
    if(node == parent[node]):
        return node
    else:
        parent[node] = findParent(parent[node])
    return parent[node]       #Path Compression
    
def union(node1,node2):
    parent1 = findParent(node1)
    parent2 = findParent(node2)
    
    rank1 = rank[parent1]
    rank2 = rank[parent2]
    if(parent1 == parent2):
        #print("Already in same component")
        return
    else:
        if(rank1 == rank2):
            rank[parent1] = rank[parent1]+1
            parent[parent2] = parent1
        elif(rank1 > rank2):
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
        parentCorrection()

        
if __name__ == "__main__":
    
    edgeNode = [(9,5,4),(4,5,1),(1,4,1),(5,4,3),(3,4,2),(2,1,2),(3,2,3),(8,3,6),(7,2,6)]
    parent = [int(i) for i in range(nodes+1)]
    
    rank = [0 for x in range(nodes+1)]
    
    edgeNode.sort(key = lambda x : x[0])
    
    print(edgeNode)
    
    mst = []
    mstCount = 0
    
    for edge in edgeNode:
        node1 = edge[1]
        node2 = edge[2]
        weight = edge[0]
        
        if(findParent(node1) != findParent(node2)):
            mstCount = mstCount + weight
            mst.append(edge)
            union(node1,node2)
    print(mstCount)
    print(mst)
        
    
    
