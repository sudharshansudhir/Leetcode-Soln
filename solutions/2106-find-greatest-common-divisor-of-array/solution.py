class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m=min(nums)
        l=max(nums)
        g=1
        for i in range(l,1,-1):
            if l%i==0 and m%i==0:
                return i
        return g
