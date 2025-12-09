class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
        ans=nums
        
        for i in range(len(ans)-1):
            if(ans[i]<target and target<ans[i+1]):
                return i+1
        if(target<nums[0]):
            return 0
        return len(nums)
