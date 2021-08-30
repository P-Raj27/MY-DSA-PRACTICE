
class Solution:

    def findMinDiff(self, A,N,M):

        start = 0
        end = M-1
        A.sort()
        minm = 999999999
        
        while end < len(A):
          minm = min(minm,A[end]-A[start])
          start+=1
          end+=1
        return(minm)
