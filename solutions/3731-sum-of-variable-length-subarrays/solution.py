class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sumi=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            for j in range(start,i+1):
                sumi+=nums[j]
        return sumi
