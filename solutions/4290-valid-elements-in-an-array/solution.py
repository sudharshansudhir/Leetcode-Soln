class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums
        c=[nums[0]]
        i=1
        while i<len(nums)-1:
            left=max(nums[:i])
            right=max(nums[i+1:])
            if nums[i]>left or nums[i]>right:
                c.append(nums[i])
            i+=1
        c.append(nums[-1])
        return c
            
