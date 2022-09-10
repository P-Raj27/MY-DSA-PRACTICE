class TrieNode():
    def __init__(self):
        self.characters = [None for x in range(26)]
        self.flag = False
class Trie():
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def charToIndex(self,ch):
        
        return ord(ch) - ord("a")
    
    def insert(self,key,count):
        
        element = self.root
        length = len(key)
        
        for i in range(length):
            #print(key[i],type(element),type(TrieNode()))
            index = self.charToIndex(key[i])
            
            if element.characters[index] == None :
                element.characters[index] = TrieNode()
                #print(count)
                count = count + 1
                #print("when i = ",key[i],type(element.characters[index]))
            element = element.characters[index]
            
        element.flag = True
        return count

if __name__ == "__main__":
    
    count = 0
    t = Trie()
    string = "abc"
    for i in range(len(string)):
        for j in range(i,len(string)):
            count = t.insert(string[j:],count)
    print(count + 1)
