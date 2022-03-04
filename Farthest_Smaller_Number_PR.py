#Farthest Smallest Element
#Better Appraoch
array=[int(x) for x in input().split()]
length=len(array)
suff_min=[0 for x in range(length)]
suff_min[length-1]=array[length-1]
for i in range(length-2,-1,-1):
    suff_min[i]=min(array[i],suff_min[i+1])
print(suff_min)
for i in range(length):
    low=i+1
    high=length-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(suff_min[mid]<array[i]):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    array[i]=ans
print(array)
