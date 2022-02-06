array=[int(x) for x in input().split(",")]
hash_table={}
max_length=0
curr_sum=0
k=3
for i in range(len(array)):
    curr_sum=curr_sum+array[i]
    if(array[i]==k and max_length==0):
        max_length=1
    if(curr_sum==k):
        max_length=i+1
    if(curr_sum in hash_table):
        max_length=max(max_length,i-hash_table[curr_sum])
    else:
        hash_table[curr_sum+k]=i
print(max_length)
print(hash_table)
