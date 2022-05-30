#House Robber 2 using DP
#Same as of (Max sum without adjacent)
max1=0
max2=0
dp=[0]*(10**6)
array=[1,2,3]
#Condition where last home(index) is excluded
array1=array[:len(array)-1]
print(array1)
dp=[0]*(10**6)
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
max1=dp[len(array1)-1]
print("max1=",max1)
#Condition where first home(0th index) is excluded
array2=array[1:]
print(array2)
dp=[0]*(10**6)
dp[0]=array[0]
dp[1]=max(array[1],dp[0])
print("dp1 is=",dp[1])
for i in range(2,len(array)):
    #print(i)
    pick=dp[i-2]+array[i]
    print("pick is = ",pick)
    print("not pick is =",notPick)
    notPick=dp[i-1]
    print("not pick is =",notPick)
    dp[i]=max(pick,notPick)
max2=dp[len(array2)-1]
print("max2",max2)
print(max(max1,max2))
