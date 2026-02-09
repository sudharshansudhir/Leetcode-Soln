class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans=[]
        mini=cost[0]
        for i in cost:
            if i<mini:
                mini=i
            ans.append(mini)
        return ans
