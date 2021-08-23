# using hashmap to store count
# accessing it with the condition of count > N/2 
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        d = {}
        for x in A:
            d[x] = 0
        for x in A:
            d[x]+=1
        
        pair=[]
        for num,count in d.items():
            pair.append([num,count])
        
        
        for x in pair:
            if x[1]>N//2:
                ans = x[0]
                flag = 1
                break
            else:
                flag = 0
        
        if flag==0:
            return(-1)
        else:
            return(ans)
