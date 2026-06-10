class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        keys=[0]*(max(nums)+1)
        for i in nums:
            keys[i]+=i
        
        r1=0
        r2=0
        m=0
        for i in keys:
            s=max(r1+i,r2)
            r1=r2
            r2=s
            m=max(m,s)
        return m