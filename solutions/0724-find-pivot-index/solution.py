class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=nums[:i]
            b=nums[i+1:]
            c=sum(a)
            d=sum(b)
            if c==d:
                return i
        return -1
