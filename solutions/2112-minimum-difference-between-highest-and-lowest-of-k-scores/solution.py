class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if(k==1):
            return 0
        i=0
        ans=max(nums)
        while i<len(nums)-k+1:
            d=nums[i+k-1]-nums[i]
            i+=1
            ans=min(ans,d)
        
        return ans

            


