array=[int(x) for x in input().split()]
stack=[]
ans=[]
stack.append(0)
ans.append(1)
for i in range(len(array)):
    while(len(stack)>0 and array[i]>=array[stack[-1]]):
        stack.pop()
    if(len(stack)<=0):
        ans.append(i+1)
    else:
        ans.append(i-stack[-1])
    stack.append(i)
print(ans)
