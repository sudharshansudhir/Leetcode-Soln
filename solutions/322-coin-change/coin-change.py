class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[float('inf')]*(amount+1) for i in range(len(coins))]
        coins.sort()

        for i in range(len(coins)):
            dp[i][0]=0
        
        one=coins[0]
        for i in range(1,amount+1):
            if i%one==0:
                dp[0][i]=i//one
            # else:
            #     dp[0][i]=-1
        
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
        # print(dp)
        # if len(coins)==1 and amount%coins[0]==1:
        #     return -1
        if dp[-1][-1]==inf:
            return -1
        return dp[-1][-1]
