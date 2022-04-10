#finding the next permutations

#array=[int(x for x in input().split())]
array=[0,1,2,5,3,3,0]
i=1
suffix_index=None
while(i<len(array)):
    if(array[i]>array[i-1]):
        suffix_index=i
    i=i+1
if(suffix_index==None):
    return False
print(suffix_index,array[suffix_index])
j=suffix_index
to_be_swapped=j
while(j<len(array)):
    if(array[j]>array[suffix_index-1]):
        to_be_swapped=j
    else:
        break
    j=j+1
print(to_be_swapped,array[to_be_swapped])
array[suffix_index-1],array[to_be_swapped]=array[to_be_swapped],array[suffix_index-1]
array_suffix=array[suffix_index:]
print(array_suffix)
array=array[0:suffix_index]+array_suffix[::-1]
print(array)

    
