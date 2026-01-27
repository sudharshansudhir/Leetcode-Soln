class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=[]
        for i in range(k):
            m=nums.pop()
            ans.append(m)
            m+=1
            nums.append(m)
        return sum(ans)
