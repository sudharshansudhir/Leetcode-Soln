class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=max(arr)
        ans=[]
        for i in range(1,m+k+1):
            if i not in arr:
                ans.append(i)
        return ans[k-1]
