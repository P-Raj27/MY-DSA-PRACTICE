# SOLUTION USING HASHMAP
IMPORTANT
#There can be solution using HEAP  as well but have to study 
#heap solution will be updated soon
# another way to solve is  Quickselect (Hoare's selection algorithm) is used to (find kth something) but very complicated so heap is the best way (HEAP )
# https://leetcode.com/problems/top-k-frequent-elements/solution/


### MY SOLUTION IS USING HASH ##
class Solution:
	def topK(self, nums, k):
	    
        hashmap = {}  # creating a hashmap to store the occurences of each element
        for x in nums:
            hashmap[x]=0
        for x in nums:
            hashmap[x]+=1
        
        
        num_freq = []   # creating a list having ([number, occurence]) elements
        for x, y in hashmap.items():
            num_freq.append([x,y]) 
        
        
        
        
        ans= []
         # sorting the numfreq list by the numbers first in descending order
        num_freq = sorted(num_freq, key=lambda x: x[0], reverse=True)
        
        # sorting the numfreq by occurence in descending order since if two num have same occurence , the number whihc is greater must be stored
        num_freq = sorted(num_freq,key=lambda x:x[1],reverse=True)  # good use of lambda function
        
        ans = []
        for i in range(k):
            ans.append(num_freq[i][0])
        
        return(ans)
