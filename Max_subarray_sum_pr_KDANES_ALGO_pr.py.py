# python-practice
#Using kdane's algorithm
#Not made by me
#Trying Kdane's Algorithm
def max_subarray(arr):
    max_so_far=0
    max_till_end=0
    for i in arr:
        max_till_end=max_till_end+i    
        if(max_till_end>max_so_far):
            max_so_far=max_till_end
        if(max_till_end<0):
            max_till_end=0
    return max_so_far
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray(arr)

#NOW the above programme wont work for all negative elements
#So we have to use a tint of dynamic Programming and modify the above.
#Note-This is an Independent Program from above
def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = 0
     
    for i in range(0,size):
        curr_max = max(a[i], curr_max + a[i])                               #So every iteration the sum is checked with the new element ,if the element is bigger than previous sum with the new element one then sub array should start from this element only
        
        print(f"When i is = {i} then curr_max = {curr_max}")
        max_so_far = max(max_so_far,curr_max)                              #so this line is used to store the maximum reached sum
         
    return max_so_far
 
# Driver function to check the above function
a = [-3,-5,0,2,1,-4]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))
 
