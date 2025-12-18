class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        for i in range(len(nums)):
            if(nums[i]==target):
                first=i
                break
        nums=nums[::-1]
        for i in range(len(nums)):
            if(nums[i]==target):
                last=len(nums)-(i+1)
                break
        return first,last
