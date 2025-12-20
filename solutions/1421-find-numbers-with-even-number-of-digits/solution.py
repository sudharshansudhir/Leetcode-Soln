class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            i=str(i)
            if(len(i)%2==0):
                ans+=1
        return ans
