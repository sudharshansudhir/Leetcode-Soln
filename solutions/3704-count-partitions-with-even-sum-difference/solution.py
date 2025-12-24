class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(0,len(nums)-1):
            left=nums[:i+1]
            right=nums[i+1:]
            s=abs(sum(left)-sum(right))
            if(s%2==0):
                c+=1
        return c
