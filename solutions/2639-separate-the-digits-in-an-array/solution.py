class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            i=str(i)
            for j in i:
                ans.append(int(j))
        return ans
