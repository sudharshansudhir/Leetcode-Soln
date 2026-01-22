class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        while nums:
            s=0
            for i in nums:
                if i>=k:
                    s+=1
            if(s==len(nums)):
                return c
            m=min(nums)
            nums.remove(m)
            c+=1

