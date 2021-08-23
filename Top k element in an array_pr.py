#Using Hash Map
#And sorting two times with different conditions.
lst=[int(x) for x in input().split()]
diction={}
fin_lst=[]
k=int(input())
for i in range(len(lst)):
    diction[lst[i]]=0
for i in range(len(lst)):
    diction[lst[i]]=diction[lst[i]]+1
print(diction)
a=[0]*len(diction)
j=0
for i in diction:                   #this loop will create a list if dictionary key and values to be sorted later.
    a[j]=[i,diction[i]]
    j=j+1
a=sorted(a,key=lambda x:x[0],reverse=True)
print(a)
a=sorted(a,key= lambda x:x[1],reverse=True)
print(a)
for i in range(k):
    fin_lst.append(a[i][0])
print(fin_lst)
    
