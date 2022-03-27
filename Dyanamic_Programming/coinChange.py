#brute force approach, dfs approach



#dynamic programming approach
def coin_change_dp(coins,amt):
    dp=[amt+1]*(amt+1)
    dp[0]=0
    for i in range(1,amt+1):
        for coin in coins:
            if(i-coin)>=0:
                dp[i]=min(dp[i],1+dp[i-coin])

    return dp[amt] if dp[amt]!=-1 else -1


coins=[1,3,4,5]
amt=7
ans=coin_change_dp(coins,amt)
print(ans)