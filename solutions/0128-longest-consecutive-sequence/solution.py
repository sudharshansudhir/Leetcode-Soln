class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        ans=[]
        t=[]
        for i in range(len(nums)-1):
            if(nums[i+1]-nums[i]==1):
                t.append(nums[i])
            else:
                t.append(nums[i])
                ans.append(t)
                t=[]
        if(nums):
            t.append(nums[-1])
        ans.append(t)
        ans.sort(key=len)
        return len(ans[-1])

