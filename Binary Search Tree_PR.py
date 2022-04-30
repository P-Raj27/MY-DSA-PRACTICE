#For finding a Variable.
#Creating a binary Tree
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def printTree(self):                                     
        if(self.left!=None):
            self.left.printTree()
        print(self.data)
        if(self.right!=None):
            self.right.printTree()
    
    def search(self,var):
        if(self.data==var):
            print("Node data is",self.data)
            print("Left Child is",self.left.data)
            print("right Child is",self.right.data)
        elif(self.data<var):
            self.right.search(var)
        else:
            self.left.search(var)
if __name__ == "__main__":
    array=[int(x) for x in input().split()]
    for i in range(len(array)):
        if(i==0):
            root=Node(array[i])
        else:
            root.insert(array[i])
        
    #root = Node(4)
    #root.insert(2)
    #root.insert(7)
    #root.insert(1)
    #root.insert(3)
    #root.insert(52)
    root.printTree()
    root.search(4)
    root.printTreePre()
