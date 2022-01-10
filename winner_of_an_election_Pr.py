def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        #lst=[str(x) for x in input().split(",")]
        #print("list is = ",lst)
        dictionary={}
        lst=[]
        for i in arr:
            dictionary[i]=dictionary.get(i,0)+1
        #print(dictionary)
        sorted_keys=sorted(dictionary.keys())
        #print(sorted_keys)
        max_value=max(dictionary.values())
        #print(max_value)
        for i in sorted_keys:
            if(dictionary[i]==max_value):
                lst.append(i)
                lst.append(max_value)
                break
        return lst
