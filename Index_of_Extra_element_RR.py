class Solution:
    def findExtra(self,a,b,n):
        for i in range(len(a)-len(b)):
           b.append(-1)
            
            
        for i in range(len(b)):
            if b[i]!=a[i]:
                return(i)
                break
        
