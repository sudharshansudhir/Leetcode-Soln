class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            if i in c.keys():
                return i
            c[i]=1
