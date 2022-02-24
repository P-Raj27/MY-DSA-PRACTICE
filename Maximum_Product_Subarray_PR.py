#Trying another approach for Maximum Product subarray
array=[6,-3,-10,0,2]
maxValue=1
minValue=1
max_Product=0
for i in range(len(array)):
    print("maxValue at 1 is above=",maxValue)
    print("minValue at 1 is above=",minValue)
    if(array[i]<0):
        maxValue,minValue=minValue,maxValue
    print(i)
    print("maxValue at 1 is=",maxValue)
    print("minValue at 1 is=",minValue)
    maxValue=max(array[i],maxValue*array[i])
    minValue=min(array[i],minValue*array[i])
    max_Product=max(maxValue,max_Product)
print(max_Product)
