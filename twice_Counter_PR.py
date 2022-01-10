def countWords(self,List, n):
        #code here
        #List=[str(x) for x in input().split()]
        #List=[str(x) for x in input().split()]
        count=0
        dictionary={}
        for i in range(0,len(List)):
            dictionary[List[i]]=dictionary.get(List[i],0)+1
        for i in dictionary.values():
            if(i==2):
                count =count +1

        
        return (count)
