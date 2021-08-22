class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    
        start = 0
        end = len(array)-1
        i=0
        
        while i<=end:
            if array[i]<a:
                array[i],array[start]=array[start],array[i]
                i+=1
                start+=1
                
            elif array[i]>b:
                array[i],array[end]=array[end],array[i]
                end-=1
            else:
                i+=1
        return(array)
