#Printing all permutation using recursion.
def helper(permutation):
    output=[]
    n=len(permutation)
    print(permutation)
    if(len(permutation)==1):
        return [permutation]
    for i in range(n):
        end=permutation[i]
        rest=permutation[:i]+permutation[i+1:]
        all_output=helper(rest)
        for content in all_output:
            output.append(content+[end])
    return output
        
        
if __name__ == "__main__":
    array=[1,2,3]
    index=0
    permutation=[]
    print(helper(array))
            
