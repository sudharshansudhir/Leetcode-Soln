class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if(1<=len(prices) and len(prices)<=10**5):
            # for i in range(len(prices)-1):
            #     if(0<=prices[i] and prices[i]<=10**4):
            #         for j in range(i+1,len(prices)):
            #             if(prices[j]-prices[i]>profit):
            #                 profit=prices[j]-prices[i]
            #     else:
            #         profit=0
            #         break
            mini=max(prices)
            maxi=0
            for i in prices:
                if(0<=i and i<=10**4):
                    mini=min(mini,i)
                    maxi=max(maxi,i-mini)
                else:
                    return 0
            return maxi
