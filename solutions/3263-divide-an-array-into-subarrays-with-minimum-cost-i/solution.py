class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a=nums[1:]
        a.sort()
        s=nums[0]
        for i in range(2):
            s+=a[i]
        return s
