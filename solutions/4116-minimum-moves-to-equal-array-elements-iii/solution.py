class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        ans=[]
        for i in nums:
            ans.append(abs(m-i))
        return sum(ans)
