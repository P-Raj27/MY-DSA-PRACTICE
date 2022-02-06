array=[int(x) for x in input().split()]
length_Array=len(array)
left=[0]*length_Array
right=[0]*length_Array
left[0]=(array[0])
for i in range(1,length_Array):
    left[i]=max(left[i-1],array[i])
right[length_Array-1]=(array[length_Array-1])
for i in range(length_Array-2,-1,-1):
    right[i]=(max(right[i+1],array[i]))
water=0
for i in range(length_Array):
    water=water+(min(left[i],right[i])-array[i])
print(water)
print(left)
print(right)
