class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            i=str(i)
            for e in i:
                ans.append(int(e))
        return ans
