#Check a sequence is graphic or not.
array=[ 4,3,3,2,2,1 ]
array.sort()
f=0
while(len(array)>0):
    array.sort()
    print(array)
    k=array.pop()
    for i in range(1,k+1):
        array[-i]=array[-i]-1
        if(array[-i]<0):
            #print("NO")
            f=1
    if(f==1):
        print("NO")
        break
    if(sum(array)==0):
        print("YES")
        break
    
    
