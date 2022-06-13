#minimum number of coins using recursion.
def helper(index,target):
    #print(index,target)
    if(index==0):
        if(target%array[index]==0):
            return target/array[index]
        else:
            return 1e9
    not_take=helper(index-1,target)
    take=1e9
    if(target>=array[index]):
        take=1+helper(index,target-array[index])
    
    return min(take,not_take)

if __name__ == "__main__":
    array=[9,6,5,1]
    index=len(array)-1
    target=11
    print(helper(index,target))
    
    
    
#minimum number of coins using DP.
array=[9,6,5,1]
target=11
dp=[[1e9 for x in range(target+1)] for x in range(len(array))]
for row in range(len(array)):
    for column in range(target+1):
        #print("hi")
        if(row==0):
            #print("hi")
            if(column%array[row]==0):
                #print("habla=",column//array[row])
                dp[row][column]=column//array[row]
            else:
                dp[row][column]=1e9
        else:
            not_take=0+dp[row-1][column]
            take=1e9
            if(column>=array[row]):
                take=1+dp[row][column-array[row]]
            #print("take is =",take)
            #print("not_take is =",not_take)
            dp[row][column]=min(take,not_take)

print(dp)            
print(dp[len(array)-1][target])
