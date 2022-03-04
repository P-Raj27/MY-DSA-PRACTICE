#Nearest Smallest Element Left.
#using stack#another faster approach
st=[]

#final_arr=[0 for x in range(len(arr))]
arr=[int(x) for x in input().split(",")]
final_arr=[0 for x in range(len(arr))]
for i in range(len(arr)):
    while(len(st)>0 and st[-1]>=arr[i]):
        st.pop()
    if(len(st)==0):
        final_arr[i]=-1
    else:
        final_arr[i]=st[-1]
    st.append(arr[i])
    print(st)
print(final_arr)
