#We have to find elements who have all its right side elements smaller or equal
lst=[int(x) for x in input().split()]
last_ele=lst[(len(lst))-1]
maxx=last_ele
fin_lst=[]
for i in range(len(lst)-1,0,-1):
    if(lst[i]>=maxx):
        fin_lst.append(lst[i])
        maxx=lst[i]
print(fin_lst[::-1])
