class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=[]
        for i in arr:
            if i==arr.count(i) and i not in ans:
                ans.append(i)
        if ans:
            return max(ans)
        return -1
