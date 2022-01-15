#Kdane's Algorithm for Maximum difference of zeros and ones in binary string
diff=0
max_difference_so_far=0
string=input()
string=list(string)
count_1=0
count_0=0
for i in range(len(string)):
    
    if(string[i]=="0"):
        diff=max(diff+1,1)
        
    if(string[i]=="1"):
        diff=max(diff-1,-1)
        
    
    max_difference_so_far=max(max_difference_so_far,diff)
if(max_difference_so_far==0):
    print(-1)
else:
    
    print(max_difference_so_far)
