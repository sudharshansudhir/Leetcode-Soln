class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        while nums:
            a=nums.pop(0)
            b=nums.pop(0)
            ans.append(b)
            ans.append(a)
        return ans

