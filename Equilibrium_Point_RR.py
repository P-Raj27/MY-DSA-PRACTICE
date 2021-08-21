
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        summ = sum(A)
        tmp = 0
        if len(A)==1:
            return(1)
        else:
            flag=0
            for i in range(len(A)-1):
                tmp = tmp + A[i] 
                if tmp == summ-tmp-A[i+1]:
                    ans=(i+2)
                    flag=1
                    break
            if flag==1:
                return ans
            else:
                return -1
