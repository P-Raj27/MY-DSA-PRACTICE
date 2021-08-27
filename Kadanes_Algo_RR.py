
# KADANES ALGORITHM (MAX SUBARRAY SUM )
#NICE EXPLAINATION BY CS DOJO
#https://www.youtube.com/watch?v=86CQq3pKSUw


class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        max_curr = max_sum = a[0]  #set current and max sum to first element 

        for i in range(1,len(a)):
    
            max_curr = max(a[i], max_curr+a[i]) # now check if current element is greater than the sum upto element which is previous of current , store the max of them 
        
            if max_curr>max_sum: # if current sum is more , then replace max sum with current sum
              max_sum = max_curr
        
        return max_sum
           
