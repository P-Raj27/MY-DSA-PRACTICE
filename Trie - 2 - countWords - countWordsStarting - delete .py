class TrieNode():
    def __init__(self):
        self.characters = [None for x in range(26)]
        self.flag = False
        self.cp = 0
        self.ew = 0
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
                cp = element.cp
                ew = element.ew
                element.characters[index] = TrieNode()
                element.characters[index].cp = 1
                element.characters[index].ew = 0
                #print("when i = ",key[i],type(element.characters[index]))
            else:
                element.characters[index].cp = element.characters[index].cp + 1
                
                element.characters[index].ew = 0
            element = element.characters[index]
            
        element.flag = True
        element.ew = 1
    
    def countWords(self,word):
        
        length = len(word)
        element = self.root
        for i in range(length):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            element = element.characters[index]
        return element.ew
    def countWordsStarting(self,word):
        
        length = len(word)
        element = self.root
        for i in range(length):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            element = element.characters[index]
        return element.cp     
    
    def search(self,word):
        
        length = len(word)
        element = self.root
        
        for i in range(length):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            element = element.characters[index]
        
        return element.flag
    
    def delete(self,word):
        
        length = len(word)
        element = self.root
        for i in range(length):
            index = self.charToIndex(word[i])
            if(element.characters[index] == None):
                return False
            else:
                element.characters[index].cp = element.characters[index].cp - 1
            element = element.characters[index]
        element.ew = element.ew - 1
        return element.cp 
        
    
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
    t.insert("apple")
    t.insert("apll")
    t.insert("apll")
    t.insert("api")
    print(t.search("apll"))
    print(t.startsWith("apr"))
    print(t.startsWith("a"))
    print(t.countWords("ap"))
    print(t.countWordsStarting("a"))
    t.delete("apple")
    t.delete("apll")
    t.delete("api")
    print(t.countWordsStarting("a"))
