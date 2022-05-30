#Concept used in here is the same as for finding all the subsequence
#i.e to consider the situation of picking or not of an element.

dp=[0]*(10**6)
array=[2,3]
dp[0]=array[0]
dp[1]=max(array[1],dp[0])
for i in range(2,len(array)):
    #print(i)
    pick=dp[i-2]+array[i]
    print("pick is = ",pick)
    print("not pick is =",notPick)
    notPick=dp[i-1]
    print("not pick is =",notPick)
    dp[i]=max(pick,notPick)
print(dp[len(array)-1])
