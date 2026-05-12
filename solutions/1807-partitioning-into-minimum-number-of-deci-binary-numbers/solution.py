class Solution:
    def minPartitions(self, n: str) -> int:
        ans=[]
        for i in n:
            ans.append(int(i))
        return max(ans)
            
