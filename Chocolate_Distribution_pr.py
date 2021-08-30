#This Problem involves Window sliding on sorted array to find the minimum difference.
m=int(input())
lst=[int(x) for x in input().split()]
lst_sorted=sorted(lst)
i=0
j=m-1
minimum=1000
while(j<len(lst)):
    mini=lst_sorted[j]-lst_sorted[i]
    if(minimum>mini):
        minimum=mini
        i_final=i
        j_final=j
    i=i+1
    j=j+1
print(lst_sorted)
print(lst_sorted[i_final:j_final+1])
        
