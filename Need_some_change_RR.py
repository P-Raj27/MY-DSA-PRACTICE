
class Solution:
	def swapElements(self, arr, n):
		start = 0
        end = start+2

        while end<len(arr):
            (arr[start],arr[end])=(arr[end],arr[start])
            start+=1
            end = start+2
            
        return(arr)
