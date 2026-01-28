class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                t1=nums[i]-1
                t2=nums[j]-1
                if t1*t2>ans:
                    ans=t1*t2
        return ans
