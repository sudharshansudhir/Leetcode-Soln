class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if(nums[k]-nums[j]==diff and nums[j]-nums[i]==diff):
                        c+=1
        return c
        
