#Sum of 4 numbers in an Array equal to number
#Idea is to have sum of all possible pairs in array
array=[int(x) for x in input().split()]
k=int(input())
hash_map={}
answer=[]

#Creating HashMap
for i in range(len(array)):
    for j in range(i+1,len(array)):
        hash_map[array[i]+array[j]]=str(i)+","+str(j)
print(hash_map)
print(hash_map.keys())
final_lst=[]
for i in hash_map.keys():
    no_duplicates=set()
    if((k-i) in hash_map.keys()):
        nums=hash_map[k-i].split(",")
        nums1=hash_map[i].split(",")
        print(nums)
        print(nums1)
        no_duplicates.add((int(nums[0])))
        no_duplicates.add((int(nums[1])))
        no_duplicates.add((int(nums1[0])))
        no_duplicates.add((int(nums1[1])))
        print(no_duplicates)
        #print("final list is=",final_lst)
        
        if(len(no_duplicates)==4 and (nums[0] not in final_lst or nums[1] not in final_lst or nums1[0] not in final_lst or nums1[1] not in final_lst)):
            answer.append(sorted([array[int(nums[0])],array[int(nums[1])],array[int(nums1[0])],array[int(nums1[1])]]))
            
            final_lst.append(nums[0])
            final_lst.append(nums[1])
            final_lst.append(nums1[0])
            final_lst.append(nums1[1])
            #print("hi")
print(answer)


