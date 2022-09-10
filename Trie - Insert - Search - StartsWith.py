class TrieNode():
    def __init__(self):
        self.characters = [None for x in range(26)]
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
            index = self.charToIndex(key[i])
            
            if element.characters[index] == None :
                element.characters[index] = TrieNode()
                #print("when i = ",key[i],type(element.characters[index]))
            element = element.characters[index]
            
        element.flag = True
    
    def search(self,word):
        
        length = len(word)
        element = self.root
        
        for i in range(length):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            element = element.characters[index]
        
        return element.flag
    
    def startsWith(self,word):
        
        length = len(word)
        element = self.root
        
        for i in range(len(word)):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            element = element.characters[index]
        return True

if __name__ == "__main__":
    
    t = Trie()
    
    t.insert("apple")
    t.insert("apll")
    print(t.search("apll"))
    print(t.startsWith("apr"))
            
