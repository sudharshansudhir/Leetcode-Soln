class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        s=abs(nums[-1]-nums[0])
        i=0
        j=1
        while j<len(nums):
            t=abs(nums[i]-nums[j])
            if t>s:
                s=t
                print(nums[i],nums[j])
            i+=1
            j+=1
        return s
