#There are two Approaches.
#1.Recursion
#2.And to better that Dynamic Programming also.


#By Using Recursion
#Edit Distance Problem using DP.
def editDistance(str1,str2,m,n):
    if(m==0):
        return n
    elif(n==0):
        return m
    else:
        if(str1[m-1]==str2[n-1]):
            return editDistance(str1,str2,m-1,n-1)
        else:
            return 1+min(editDistance(str1,str2,m,n-1),editDistance(str1,str2,m-1,n),editDistance(str1,str2,m-1,n-1))
if __name__=="__main__":
    str1=input()
    str2=input()
    print(editDistance(str1,str2,len(str1),len(str2)))





#Using Dynamic Programming.
#Edit Distance Problem using DP.
str1=input()
str2=input()
m=len(str1)
n=len(str2)
dp=[[0 for x in range(n+1)] for x in range(m+1)]
print(dp)
for i in range(m+1):
    for j in range(n+1):
        if(i==0):
            dp[i][j]=j
        if(j==0):
            dp[i][j]=i
        if(str1[i-1]==str2[j-1]):
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i][j])
print(dp[m][n])
