#Distinct Subsequence.
#Using Recursion

def helper(i,j):
    if(j<0):
        return 1
    if(i<0):
        return 0
    if(s1[i]==s2[j]):
        return (helper(i-1,j-1)+helper(i-1,j))
    else:
        return (helper(i-1,j))
    
if __name__ == "__main__":
    
    s1="banana"
    s2="ban"
    print(helper(len(s1)-1,len(s2)-1))
    
    
    
    
#Distinct Subsequence
#Using Dp
#There is no such extra logic just understand the requirement and make the recursion.

str1="banana"
str2="ban"
l1=len(str1)
l2=len(str2)

dp=[[0 for x in range(l2+1)] for x in range(l1+1)]

for row in range(l1+1):
    for column in range(l2+1):
        if(row==0):
            dp[row][column]=0
        #print(column)
        if(column==0):
            #print(column)
            dp[row][column]=1
            print(f"row is ={row} and col ={column}",dp[row][column])
        else:
            if(str1[row-1]==str2[column-1]):
                dp[row][column]=dp[row-1][column-1]+dp[row-1][column]
            else:
                dp[row][column]=dp[row-1][column]
print(dp[l1][l2])
