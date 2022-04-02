#Score of parenthesis
string=input()
i=0
ans=0
stack=[]
for i in range(len(string)):
    if(string[i]=="("):
        stack.append(string[i])
    else:
        if(stack[-1]=="("):
            stack.pop()
            stack.append(1)
        else:
            count=0
            while(stack[-1]!="("):
                count=count+int(stack[-1])
                stack.pop()
            stack.pop()
            stack.append(2*count)
print(sum(stack))
                
            
        
        
