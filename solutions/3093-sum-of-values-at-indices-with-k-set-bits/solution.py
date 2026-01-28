class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        l=len(nums)
        ans=0
        for i in range(l):
            s=bin(i)[2:]
            if s.count("1")==k:
                ans+=nums[i]
        return ans
