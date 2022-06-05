#Subset sum to a target using DP
array=[9,7,0,3,9,8,6,5,7,6]
target=31
dp=[[0 for x in range(target+1)] for x in range(len(array)+1)]
print(dp)
for row in range(len(array)+1):
    for column in range(target+1):
        if(row==0 and column==0):
            dp[row][column]=1
        elif(row==0):
            dp[row][column]=0
        
        elif(column>=array[row-1]):
            
            dp[row][column]=dp[row-1][column-array[row-1]]+dp[row-1][column]
        else:
            #print(column-array[row-1])
            dp[row][column]=dp[row-1][column]
            
print(dp)
print("t",target)
print("l",len(array))
print(dp[len(array)][target])
