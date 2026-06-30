class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans={"a":0,"b":0,"c":0}
        left=0
        n=len(s)
        a=0
        for r in range(n):
            ans[s[r]]+=1

            while ans["a"]>0 and ans["b"]>0 and ans["c"]>0:
                ans[s[left]]-=1
                left+=1
            a+=left
        return a

