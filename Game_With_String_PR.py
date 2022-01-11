from queue import PriorityQueue
s=input()
k=int(input())
count=dict()
for ch in s:
    count[ch]=1+count.get(ch,0)
print(count)
    
resl=PriorityQueue()
for key,v in count.items():
    print("value going in queue is",-1*v)
    resl.put(-1*v)
#for i in range(3):
 #   print("queue element is=",resl.get())

        
for i in range(k):
    x=resl.get()+1
    print(x)
    resl.put(x)
            
res=0
while not resl.empty():
    n=resl.get()
    print(n)
    res+=n*n
print(res)
