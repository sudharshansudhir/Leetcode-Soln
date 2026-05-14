class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        m=max(nums)
        flag=True
        for i in nums:
            if i==m:
                continue
            elif nums.count(i)>=2:
                flag=False
        if m+1==len(nums) and nums.count(m)==2 and flag:
            return True
        return False
