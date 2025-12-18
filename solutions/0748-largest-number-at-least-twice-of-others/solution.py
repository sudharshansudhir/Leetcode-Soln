class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if(not i==j and nums[j]*2<=nums[i]):
                    c+=1
            if(c==len(nums)-1):
                return i
        return -1

