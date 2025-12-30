class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        s=nums[:]
        i=0
        t=[]
        while nums and i<len(nums):
            if(nums[i] not in t):
                t.append(nums[i])
                nums.remove(nums[i])
            else:
                i+=1
            if(i==len(nums)):
                i=0
                ans.append(t)
                t=[]
        return ans
        
