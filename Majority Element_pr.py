lst=[int(x) for x in input().split()]
freq={}
n=len(lst)
f=0
for i in lst:
    if(i in freq):
        freq[i]=freq[i]+1
    else:
        freq[i]=1
for i in freq:
    if(freq[i]>n//2):
        print(i)
        f=1
if(f==0):
    print(-1)

    
        
    
    
