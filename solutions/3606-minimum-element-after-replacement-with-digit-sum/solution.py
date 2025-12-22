class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            i=str(i)
            s=0
            for j in i:
                s+=int(j)
            ans.append(int(s))

        return min(ans)


