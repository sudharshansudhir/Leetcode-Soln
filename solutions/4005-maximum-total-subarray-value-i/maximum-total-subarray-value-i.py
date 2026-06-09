class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        mi=min(nums)
        d=mx-mi
        return d*k