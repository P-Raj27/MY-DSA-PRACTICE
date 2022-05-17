#Trying ABove question using Dynamic Programming
A="YX"
B="X"
C="XXY"
m=len(A)
n=len(B)
if(m+n==len(C)):
    matrix=[[False for x in range(n+1)] for x in range(m+1)]
    print(matrix)
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 and j==0):
                matrix[i][j]=True
            elif(i==0):
                if(B[j-1]==C[j-1]):
                    matrix[i][j]=matrix[i][j-1]
            elif(j==0):
                if(A[i-1]==C[i-1]):
                    matrix[i][j]=matrix[i-1][j]
            else:
                if(A[i-1]==C[i+j-1] and B[j-1]!=C[i+j-1]):
                    matrix[i][j]=matrix[i-1][j]
                elif(A[i-1]!=C[i+j-1] and B[j-1]==C[i+j-1]):
                    matrix[i][j]=matrix[i][j-1]
                elif(A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]):
                    matrix[i][j]=(matrix[i][j-1] or matrix[i-1][j])
print(matrix[m][n])
            
