def minSteps(self, S):
		# code here
		s=S
        dp=[len(s) for x in range(len(s))]
        s1=""
        s2=""
        s1=s1+s[0]
        dp[0]=1
        for i in range(1,len(s)):
            s1=s1+s[i]
            s2=s[i+1:i+1+i+1]
            dp[i]=min(dp[i],dp[i-1]+1)
            if(s1==s2):
                dp[2*i+1]=min(dp[i]+1,dp[2*i+1])
        return(dp[len(s)-1])
