class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        while costs and coins>0:
            p=costs.pop(0)
            if p<=coins:
                coins-=p
                c+=1
            else:
                break
        return c
