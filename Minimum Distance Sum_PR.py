#Minimum Path sum in a grid to reach a location
points=[[1,2,3],[4,5,6]]
row=len(points)
column=len(points[0])
dp=[[0 for x in range(column)] for x in range(row)]
print(dp)
for i in range(row):
    for j in range(column):
        if(i==0 and j==0):
            dp[i][j]=points[i][j]
        else:
            if((i-1)>=0 and (j-1)>=0):
                dp[i][j]=min(dp[i-1][j]+points[i][j],dp[i][j-1]+points[i][j])
                print(f"dp value at {i} and {j} is =",dp[i][j])
            elif(i-1<0):
                dp[i][j]=(dp[i][j-1]+points[i][j])
            elif(j-1<0):
                dp[i][j]=(dp[i-1][j]+points[i][j])
                
                
print(points)
print(dp)
print(dp[1][1])
print(dp[row-1][column-1])
