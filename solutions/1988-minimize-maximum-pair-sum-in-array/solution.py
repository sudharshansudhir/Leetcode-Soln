class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        s=[]
        while i<j:
            s.append(nums[i]+nums[j])
            i+=1
            j-=1
        return max(s)
