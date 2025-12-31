class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        while True:
            if nums[i]==target:
                return i
            i+=1
            if(i==len(nums)):
                return -1
