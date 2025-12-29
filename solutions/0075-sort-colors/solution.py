class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums
        i=0
        while i<len(nums)-1:
            if(nums[i]>nums[i+1]):
                t=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=t
                i+=1
            else:
                i+=1
        return nums
            
