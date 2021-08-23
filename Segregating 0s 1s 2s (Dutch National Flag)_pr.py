#Using Dutch National Flag Algorithm
#We are setting three pointers
arr=[int(x) for x in input().split()]
a=arr
left=0
mid=0
right=len(arr)-1
while(mid<=right):          #Condition Prevents the pointers to cross.
  if(a[mid]==0):
    a[mid],a[left]=a[left],a[mid]               #swapping if 0 comes in different section.
    mid=mid+1
    left=left+1
  elif(a[mid]==1):                              #swapping if 1 comes in different section
    mid=mid+1 
  else:
    a[mid],a[right]=a[right],a[mid]             #Swapping for 2 in different section
    right=right-1
print(a)  
