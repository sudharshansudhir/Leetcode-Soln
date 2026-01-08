class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c=0
        for i in range(len(s)):
            if s[i] in t:
                k=t.index(s[i])
                t=t[:k]+t[k+1:]
            else:
                c+=1
        return c
