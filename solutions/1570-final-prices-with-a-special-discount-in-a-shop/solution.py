class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)-1):
            flag=False
            for j in range(i+1,len(prices)):
                if(prices[j]<=prices[i] and not flag):
                    ans.append(prices[i]-prices[j])
                    flag=True
            if not flag:
                ans.append(prices[i])
        ans.append(prices[-1])
        return ans
