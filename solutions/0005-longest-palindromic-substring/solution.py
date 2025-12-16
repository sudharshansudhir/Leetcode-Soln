class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        c=0
        if len(s)==1:
            return s
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                t=s[i:j+1]
                if(t==t[::-1]):
                    if(len(t)>c):
                        c=len(t)
                        longest=t
        print(longest)
        if(longest==""):
            longest=s[0]
        return longest
