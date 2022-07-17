#Distinct subsequence of a string.
string = "gpfumxybqfbajodenoukpsnxaknscmmkbreno"
dic={}
dp=[0]*(len(string)+1)
for i in range(len(string)):
    if(string[i] in dic):
        dp[i+1]=dp[i]*2-dp[dic[string[i]]-1]
    else:
        dp[i+1]=dp[i]*2+1
    dic[string[i]]=i+1

    
    
print(dp[-1]+1)
#print(set(lst))
            
