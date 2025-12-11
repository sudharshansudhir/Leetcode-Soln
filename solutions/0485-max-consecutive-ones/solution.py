class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=max(nums)
        c=0
        for i in range(len(nums)):
            if(nums[i]==1):
                c+=1
            else:
                c=0
            if(maxi<c):
                maxi=c
        print(maxi)
        return maxi



