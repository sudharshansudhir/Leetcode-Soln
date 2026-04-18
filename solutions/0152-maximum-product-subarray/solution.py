class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref=1
        suff=1
        n=len(nums)
        maxi=nums[0]
        for i in range(n):
            pref=pref*nums[i]
            suff=suff*nums[n-i-1]
            
            maxi=max(maxi,max(suff,pref))
            if pref==0:
                pref=1
            if suff==0:
                suff=1
        return maxi
