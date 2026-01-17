class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0
        c=0
        while i+3<=len(nums):
            if(nums[i]==0):
                for n in range(i,i+3):
                    if nums[n]==0:
                        nums[n]=1
                    else:
                        nums[n]=0
                c+=1
            i+=1
        if 0 not in nums:
            return c
        return -1
          

