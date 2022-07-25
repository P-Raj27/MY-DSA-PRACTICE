#Buying and Selling stock using 3D Dp.

prices = [3,3,5,0,0,3,1,4]
#prices = [1,2,3,4,5]
#prices = [4,3,2,1]

n=len(prices)
cap = 2
buy = 1

#Creating 3d Dp.
dp = [[[0 for cap in range(cap+1)] for buy in range(2)] for index in range(n+1)]
print(dp)

for index in range(n,-1,-1):
    for buy in range(2):
        for cap in range(1,cap+1):
            if(index == len(prices) or cap == 0):
                #print("index =", index)
                dp[index][buy][cap]=0
            elif(index == len(prices)-1 and buy == 0):
                   dp[index][buy][cap]=(prices[index])
            elif(index == len(prices)-1 and buy == 1):
                    dp[index][buy][cap]=0
            else:
                if (buy == 1):  #Only option to buy or not(Not allowed to sell)
                    if_buy = -prices[index]+dp[index+1][0][cap]
                    if_not_buy = dp[index+1][1][cap]
                    profit = max(if_buy,if_not_buy)
                    dp[index][buy][cap]=profit
                else:
                    if_sell = prices[index]+dp[index+1][1][cap-1]
                    if_not_sell = dp[index+1][0][cap]
                    profit = max(if_sell,if_not_sell)
                    dp[index][buy][cap]= profit
#print(dp)
print(dp[0][1][cap])
            
            
