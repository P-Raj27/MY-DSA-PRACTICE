#Trying Above Question with another Approach
pushed=[1,2,3,4,5]
popped=[4,5,3,2,1]
stack=[]
j=0
for i in pushed:
    stack.append(i)
    #print("pushing in stack",stack)
    while(j<len(popped) and len(stack)>0 and popped[j]==stack[-1]):
        #print("Just Before Popping",stack)
        stack.pop()
        j=j+1
#print(stack)
if(len(stack)>0):
    print(False)
else:
    print(True)
    
