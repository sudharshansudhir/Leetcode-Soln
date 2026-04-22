class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)[2:]
        g=bin(goal)[2:]
        a=0
        if len(s)<len(g):
            t=len(g)-len(s)
            tt="0"*t
            tt+=s[:]
            s=tt[:]
        elif len(g)<len(s):
            t=len(s)-len(g)
            tt="0"*t
            tt+=g[:]
            g=tt[:]

        for i in range(len(s)):
            if not s[i]==g[i]:
                a+=1
        return a
