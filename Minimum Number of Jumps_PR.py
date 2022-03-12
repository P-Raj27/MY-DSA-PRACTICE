#Minimum number of jumps.
array=[int(x) for x in input().split(",")]
maxReach=array[0]
flag=0
jump=1
step=array[0]
for i in range(1,len(array)):
    if(i==len(array)-1):
        print(jump)
        flag=1
    maxReach=max(maxReach,i+array[i])
        
    step=step-1
    if(step==0):
        jump=jump+1
    #    print(f"{jump} when i is {i}")
        if(i>=maxReach):
            print("not possible to reach")
        step=maxReach-i
   # print(f"{step} is step when {maxReach}")
if(flag==0):
    print("not possible to reach")

    
    
    
