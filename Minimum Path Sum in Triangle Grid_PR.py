#Minimum Path sum in a right angle triangle to reach a location
points=[[-1],[3,2],[-3,1,-1]]

row=len(points)
column=len(points[row-1])
dp=[]
for i in range(len(points)):
    dp.append([0 for x in range(len(points[i]))])    
print(dp)

for i in range(row):
    column=len(points[i])
    for j in range(column):
        #Condition 1
        if(i==0 and j==0):
            dp[i][j]=points[i][j]
        #Condition 2    
        elif(j==0):
            print(dp[i-1][j],points[i][j])
            dp[i][j]=dp[i-1][j]+points[i][j]
        #Condition 3
        elif(j==column-1):
            dp[i][j]=dp[i-1][j-1]+points[i][j]
        #Cndition 4
        else:
            dp[i][j]=min(dp[i-1][j]+points[i][j],dp[i-1][j-1]+points[i][j])
            
print(dp)
print(min(dp[row-1]))
        
                
                
