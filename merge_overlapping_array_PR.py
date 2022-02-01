#merge overlapping interval
array=[[1,4],[2,3]]
s=[]
sorted_array=sorted(array,key=lambda x:x[0])
print(sorted_array)
s.append(sorted_array[0][0])
s.append(sorted_array[0][1])
for i in range(1,len(array)):
    start=sorted_array[i][0]
    end=sorted_array[i][1]
    print("start is=",start)
    print("end is=",end)
    pop_value=s.pop()
    if(start<=pop_value):
        s.append(max(end,pop_value))
    else:
        s.append(pop_value)
        s.append(start)
        s.append(end)
print(s)
final_list=[]
j=0
for i in range(len(s)):
    
    if(i%2==0):
        start=s[i]
    else:
        end=s[i]
    j=j+1
    if(j==2):
        j=0
        final_list.append([start,end])
print(final_list)
    
