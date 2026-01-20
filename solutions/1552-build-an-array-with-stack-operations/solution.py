class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        ans=[]
        for i in range(1,n+1):
            s.append(i)
            ans.append("Push")
            if s[-1] not in target:
                s.pop()
                ans.append("Pop")
            if target==s:
                return ans
        return ans

