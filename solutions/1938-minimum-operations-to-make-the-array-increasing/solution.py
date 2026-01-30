class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            if(nums[i]>=nums[i+1]):
                t=(nums[i]-nums[i+1])
                ans+=t+1
                nums[i+1]=t+nums[i+1]+1
                # print(nums)
        return ans

