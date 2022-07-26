#Longest Increasing Subsequence using recursion.
#Understand the Recursion part first then go for dp.

def helper(ind,prev):
    
    if (ind == len(array)):
        return 0
    else:
        not_take = 0+helper(ind+1,prev)
        if(array[ind] > prev):
            take = 1+helper(ind+1,array[ind])
            return max(take,not_take)
        return not_take

if __name__ == "__main__":
    
    array = [7,7,7,7,7,7,7]
    prev = -1
    print(helper(0,prev))

    
    
    
    
 #Using Dp   
array = [10,9,2,5,3,7,101,18]
leng=len(array)
dp =[[0 for x in range(leng+1)] for x in range(leng+1)]

print(dp)

for ind in range(leng-1,-1,-1):
    for prev in range(ind-1,-2,-1):
        if (ind == len(array)):
            dp[ind][prev]=0
        else:
            not_take = 0+dp[ind+1][prev+1]
            if(prev == -1 or array[ind] > array[prev]):
                take = 1+dp[ind+1][ind+1]
                dp[ind][prev+1]=max(take,not_take)
            else:
                dp[ind][prev+1]=not_take
print(dp)
print(dp[0][0])
           
