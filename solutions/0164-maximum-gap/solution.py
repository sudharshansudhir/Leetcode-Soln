class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        diff=0
        for i in range(len(nums)-1):
            if(nums[i+1]-nums[i]>diff):
                diff=nums[i+1]-nums[i]
        return diff
