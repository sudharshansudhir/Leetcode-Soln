class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        for k in range(len(s)):
            ss=s[k:]
            t=""
            n=0
            for i in ss:
                if i not in t:
                    t+=i
                    n+=1
                else:
                    if(m<n):
                        m=n
                        n=0
                    t=i
                    n=1
                    break
            if(n>m):
                m=n
        return m
