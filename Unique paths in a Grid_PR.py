#Unique Paths in a Grid using recursion
def helper(row,column):
    #base case
    if(row==0 and column==0):
        #print("hi")
        return 1
    if(row<0 or column<0):
        
        return 0
    up=helper(row-1,column)
    down=helper(row,column-1)
    return up+down

if __name__=="__main__":
    row=3
    column=7
    print(helper(row-1,column-1))
    
    
    
    
    
#Unique Paths in a Grid using DP
row=3
column=2
dp=[[0 for x in range(column+1)] for x in range(row+1)]
print(dp)
for i in range(row+1):
    for j in range(column+1):
        if(i==0 or j==0):
            dp[i][j]=0
        elif(i==1 and j==1):
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[row][column])
