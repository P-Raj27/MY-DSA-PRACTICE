#Bit Magic Josephus Problem
n=int(input())
person=[int(x) for x in range(n)]
k=int(input())
k=k-1
start=0
def killer(person,k,start):
    if(len(person)==1):
        ans=(person[0]+1)
        return ans
    else:
        start=(start+k)%(len(person))
        person.pop(start)
        return killer(person,k,start)
killer(person,k,start)
    
