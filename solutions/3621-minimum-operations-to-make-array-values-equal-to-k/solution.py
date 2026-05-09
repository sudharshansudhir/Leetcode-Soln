class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=[]
        for i in nums:
            if i>k and i not in s:
                s.append(i)
            elif i<k:
                return -1
        return len(s)
                
