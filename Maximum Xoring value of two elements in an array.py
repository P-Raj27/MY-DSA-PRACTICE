#Bit Prerequest for Trie.
#Maximum XOR.

class TrieNode():
    def __init__(self):
        self.characters = [None for x in range(2)]
        self.flag = False
class Trie():
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def charToIndex(self,ch):
        
        return ord(ch) - ord("a")
    
    def insert(self,key):
        
        element = self.root
        length = len(key)
        
        for i in range(length):
            #print(key[i],type(element),type(TrieNode()))
            #index = self.charToIndex(key[i])
            
            if element.characters[int(key[i])] == None :
                element.characters[int(key[i])] = TrieNode()
                #print("when i = ",key[i],type(element.characters[index]))
            element = element.characters[int(key[i])]
            
        element.flag = True
        
    def xoring(self,binary):
        
        element = self.root
        length = len(binary)
        string = ""
        
        for i in range(length):
            
            if(binary[i] == "0"):
                if (element.characters[1] == None):
                    string = string + "0"
                    element = element.characters[0]
                else:
                    string = string + "1"
                    element = element.characters[1]
            else:
                if (element.characters[0] == None):
                    string = string + "0"
                    element = element.characters[1]
                else:
                    string = string + "1"
                    element = element.characters[0]
        return string


if __name__ == "__main__":

    array = [9,8,7,5,4]
    bin_array = []
    t = Trie()
    for i in array:
        bin_array.append("{:05b}".format(i))
    print(bin_array)
    for i in bin_array:
        t.insert(i)
    
    xoring_list = []
    for i in bin_array:
        xoring_list.append(t.xoring(i))
    
    print(xoring_list)
    
    for i in range(len(xoring_list)):
        
        xoring_list[i] = int(xoring_list[i],2)
    print(max(xoring_list))
        


