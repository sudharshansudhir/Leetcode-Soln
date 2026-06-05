class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a=nums[:3]
        ans=1
        for i in a:
            ans*=i
        t=1
        m1=min(nums)
        nums.remove(m1)
        m2=min(nums)
        maxi=max(nums)
        return max(ans,(m1*m2*maxi))