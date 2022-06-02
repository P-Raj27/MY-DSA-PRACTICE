#minimum fallng path using DP.
#This is for fixed starting point and fixed end point.
points=[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
rows=len(points)
columns=len(points[0])
dp=[[0 for i in range(columns)] for i in range(rows)]

for row in range(rows):
    for column in range(columns):
        if(row==0):
            dp[row][column]=points[row][column]
        elif(column==0):
            dp[row][column]=min(dp[row-1][column]+points[row][column],dp[row-1][column+1]+points[row][column])
        elif(column==columns-1):
            dp[row][column]=min(dp[row-1][column]+points[row][column],dp[row-1][column-1]+points[row][column])
        else:
            dp[row][column]=min(dp[row-1][column]+points[row][column],dp[row-1][column-1]+points[row][column],dp[row-1][column+1]+points[row][column])
            
            
print(min(dp[rows-1]))

#maximum fallng path using DP.
#This is for fixed starting point and fixed end point.
points=[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
rows=len(points)
columns=len(points[0])
dp=[[0 for i in range(columns)] for i in range(rows)]

for row in range(rows):
    for column in range(columns):
        if(row==0):
            dp[row][column]=points[row][column]
        elif(column==0):
            dp[row][column]=max(dp[row-1][column]+points[row][column],dp[row-1][column+1]+points[row][column])
        elif(column==columns-1):
            dp[row][column]=max(dp[row-1][column]+points[row][column],dp[row-1][column-1]+points[row][column])
        else:
            dp[row][column]=max(dp[row-1][column]+points[row][column],dp[row-1][column-1]+points[row][column],dp[row-1][column+1]+points[row][column])
            
            
print(max(dp[rows-1]))
