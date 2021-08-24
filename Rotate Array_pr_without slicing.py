lst=[int(x) for x in input().split()]
n=len(lst)
d=int(input())
d=d%n
start=0
end=d-1
while(start<end):
    lst[start],lst[end]=lst[end],lst[start]
    start=start+1
    end=end-1
start=d
end=n-1
while(start<end):
    lst[start],lst[end]=lst[end],lst[start]
    start=start+1
    end=end-1
start=0
end=n-1
while(start<end):
    lst[start],lst[end]=lst[end],lst[start]
    start=start+1
    end=end-1
print(lst)
    
