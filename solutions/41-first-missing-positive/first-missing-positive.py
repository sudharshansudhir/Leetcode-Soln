class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
        n=len(nums)
        for i in range(1,n+1):
            v=dict.get(i,0)
            if v==0:
                return i
        return n+1

