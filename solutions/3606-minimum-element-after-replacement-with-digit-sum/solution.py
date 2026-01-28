class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            i=str(i)
            j=0
            for ii in i:
                j+=int(ii)
            ans.append(j)
        return min(ans)

