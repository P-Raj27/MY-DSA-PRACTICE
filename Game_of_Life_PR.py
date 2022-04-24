#Game of Life.
#The main click here is to find all the neighbours values for each.
#Here we are using a list of tuples to traverse through neighbours.

matrix=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
neighbours=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
m=len(matrix)
n=len(matrix[0])
for i in range(m):
    for j in range(n):
        liveCount=0
        for r,c in neighbours:
            nr,nc=i+r,j+c
            if(0<=nr<m and 0<=nc<n and abs(matrix[nr][nc])==1):
                liveCount=liveCount+1
        if(matrix[i][j]==1):
            if(liveCount<2 or liveCount>3):
                matrix[i][j]=-1
        else:
            if(liveCount==3):
                matrix[i][j]=2
print(matrix)
for i in range(m):
    for j in range(n):
        if(matrix[i][j]==-1):
            matrix[i][j]=0
        elif(matrix[i][j]==2):
            matrix[i][j]=1
print(matrix)
        
                
                
