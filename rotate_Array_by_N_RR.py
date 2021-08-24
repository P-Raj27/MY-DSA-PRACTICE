# ONE OF THE SOLUTION OF THIS PROBLEM IS AN ALGORITHM CALLED " JUGGLING ALGORITHM" O(N) Time and O(1) space
# IT WILL BE UPDATED SOON





###########################    SOLUTION 1    #####################################################################################
#O(N*D) SOLUTION
# @ROHIT ROSHAN (Any doubts U can clarify)
# start holds the value of D (no by which to rotate)
# D-1 is the index of last element to be rotate starting from 0
# until we reach start = 0 i.e all the n elements are pushed back we repeat the process
start = D-1
end = N-1
while start>=0:
    for i in range(start,end): # this loops takes each element which is to be sent back to its desired position at the back of the array
        A[i],A[i+1]=A[i+1],A[i]
    start-=1
    end-=1
return A

###########################    SOLUTION 2   #####################################################################################

#O(N) solution
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
                
        start = 0
        end = D-1
        #reverse first D element
        while start<end:
            A[start],A[end]=A[end],A[start]
            start+=1
            end-=1
        end2 = len(A)-1
        start2 = D
        
        #reverse element after D
        while start2<end2:
            A[start2],A[end2]=A[end2],A[start2]
            start2+=1
            end2-=1
            
        #reverse whole array
        start3=0
        end3=len(A)-1
        while start3<end3:
            A[start3],A[end3]=A[end3],A[start3]
            start3+=1
            end3-=1



        return(A)
      
      
############################ SOLUTION  3 #########################
      # Pythonic Way 
      
      tmp = A[:D]
      A = A[D:]
      A.extend(tmp)
      print(A)
      
 li=[1,2,3,4,5]
 li[2:]+li[:2]
output = [3, 4, 5, 1, 2]
 li[-2:]+li[:-2]
output = [4, 5, 1, 2, 3]
      
######################### SOLUTION  4 ###########################
      
# USING DEQUE 
# CHECK FOR MISTAKES
import collections
dq = collections.deque(A)

A = [1,2,3,4,5]
D = 2
tmp = []
for i in range(D):
    tmp.append(dq.popleft())

for i in range(len(tmp)):
    dq.append(tmp[i])

print(list(dq))

####################### ANOTHER SOLUTION USING DEQUE #############################



from collections import deque
>>> d=deque([1,2,3,4,5])
>>> d
deque([1, 2, 3, 4, 5])
>>> d.rotate(2)
>>> d
deque([4, 5, 1, 2, 3])
>>> d.rotate(-2)
>>> d
deque([1, 2, 3, 4, 5])


