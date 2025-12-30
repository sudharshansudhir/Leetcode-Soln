class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(not i==j):
                    if(abs(nums[j]-nums[i])==k):
                        c+=1
        return c
