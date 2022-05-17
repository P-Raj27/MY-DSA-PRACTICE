#The Famous KnapSack Problem
weights=[10,20,30]
values=[60,100,120]
max_weight=50
n=len(values)
matrix=[[0 for x in range(max_weight+1)] for x in range(n+1)]
for value in range(n+1):
    for weight in range(max_weight+1):
        if(value==0 or weight==0):
            matrix[value][weight]=0
        elif(weights[value-1]<=weight):
            matrix[value][weight]=max(values[value-1]+matrix[value-1][weight-weights[value-1]],matrix[value-1][weight])
        else:
            matrix[value][weight]=matrix[value-1][weight]
print(matrix[n][max_weight])
