class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # nums=list(set(nums))
        a=[]
        nums.sort()
        c=0
        while nums and c<k:
            aa=nums.pop()
            if aa not in a:
                a.append(aa)
                c+=1
        return a
