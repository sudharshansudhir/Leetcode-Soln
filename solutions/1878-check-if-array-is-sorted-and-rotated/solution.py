class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        t=nums[:]
        t.sort()
        flag=False
        for i in range(n):
            s=t[n-i:]+t[:n-i]
            print(s)
            if(s==nums):
                flag=True
                break
        return flag

