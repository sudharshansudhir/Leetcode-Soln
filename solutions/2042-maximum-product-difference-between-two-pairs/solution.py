class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums=list(set(nums))
        nums.sort()
        m1=nums[0]
        m2=nums[1]
        ma1=nums[-1]
        ma2=nums[-2]
        return (ma1*ma2)-(m1*m2)

