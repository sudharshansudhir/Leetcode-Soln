class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=min(nums)
        i=0
        while i<len(nums):
            sums=sums+nums[i]
            if sums>maxi:
                maxi=sums
            if sums<0:
                sums=0
            i+=1
            # if sums<0:
            #     maxi=max(sums,maxi)
            #     sums=0
            #     i+=1
            #     continue
            # maxi=max(maxi,sums)
            # i+=1
        return maxi

