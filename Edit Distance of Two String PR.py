#edit distance using dp.

s1="ecfbefdcfca"
s2="badfcbebbf"

rows=len(s1)
columns=len(s2)

dp = [[0 for x in range(columns+1)] for x in range(rows+1)]

print(dp)

for i in range(rows+1):
    for j in range(columns+1):
        if(i==0):
            dp[i][j]=j
        if(j==0):
            #print(i)
            dp[i][j]=i
        if(s1[i-1]==s2[j-1]):
            dp[i][j]=0+dp[i-1][j-1]
        else:
            #insert operation
            insert=1+dp[i][j-1]
            #delete operation
            delete=1+dp[i-1][j]
            #replace operation
            replace=1+dp[i-1][j-1]
            dp[i][j]=min(insert,delete,replace)
print(dp)
print(dp[i][j])
        
