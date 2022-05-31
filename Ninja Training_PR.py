#Ninja Training using Dynamic Programming.
matrix=[[10,40,70],[20,50,80],[30,60,90]]
n=len(matrix)
dp=[[0,0,0] for x in range(n)]
print(dp)
print(dp[1][0])
maxx=0
last=-1
for i in range(n):
    for j in range(3):
        if(i==0):
            dp[i][j]=matrix[i][j]
        else:
            maxi=0
            for k in range(3):
                if(k!=j):
                    points=matrix[i][j]+dp[i-1][k]
                    maxi=max(maxi,points)
            print(i,j)
            dp[i][j]=maxi
for i in range(3):
    maxx=max(maxx,dp[n-1][i])
print(maxx)


#Ninja Training using Recursion.
def helper(day,last):
    if(day==0):
        maxi=0
        for i in range(3):
            if(i!=last):
                maxi=max(maxi,task[0][i])
        return maxi
    else:
        maxi=0
        for i in range(3):
            if(i!=last):
                points=task[day][i]+helper(day-1,i)
                maxi=max(maxi,points)
        return maxi
if __name__ == "__main__":
    
    task=[[10,40,70],[20,50,80],[30,60,90]]
    day=len(task)-1
    maxx=0
    for i in range(3):
        maxx=max(maxx,helper(day,i))
    print(maxx)
        
        
    
        


