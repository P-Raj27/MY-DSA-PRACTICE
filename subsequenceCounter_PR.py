#Subsequence Counter with two pointer.
p1=0
p2=0
string=input()
count=0
while(p1<len(string)):
    if(p1!=p2):
        if(string[p1]=="1" and string[p2]=="1"):
            count=count+1
            print(string[p1:p2+1])
    p2=p2+1
    if(p2==len(string)):
        p1=p1+1
        p2=p1
print(count)

#After Analyzing the string.
string=(input())
count=0
for i in string:
    if(i=="1"):
        count=count+1
print(count)
summ=0
for i in range(count-1,0,-1):
    summ=summ+i
print(summ)
    
            
