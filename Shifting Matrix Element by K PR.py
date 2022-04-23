#Shifitng Element in Matrix
#THe Idea is to flatten the Matrix to a single list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
k=1
k=k%(m*n)
m=len(matrix)
n=len(matrix[0])
flatten=[]
for row in matrix:
    flatten=flatten+row
print(flatten)
flatten=flatten[len(flatten)-(k):]+flatten[:len(flatten)-(k)]
print(flatten)
count=0
final_matrix=[]
temp=[]
final_matrix=[flatten[i*n : (i*n)+n] for i in range(m)]
print(final_matrix)
