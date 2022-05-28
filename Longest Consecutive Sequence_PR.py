#longest Consecutive Sequence
array=[100,4,200,1,3,2]
array_set=set(array)
max_count=0

for i in range(len(array)):
    res=array[i]
    count=0
    if(array[i]-1 in array_set):
        continue
    else:
        while(res in array_set):
            res=res+1
            #print(res)
            count=count+1
        max_count=max(max_count,count)
print(max_count)
            
            
