class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        g1=nums[:]
        g2=nums[:]
        i=0
        sm=[]
        lr=[]
        while i<k:
            m=min(g1)
            ma=max(g2)
            g1.remove(m)
            g2.remove(ma)
            sm.append(m)
            lr.append(ma)
            i+=1
        if i<k:
            return 0
        return abs(sum(sm)-sum(lr))
        

