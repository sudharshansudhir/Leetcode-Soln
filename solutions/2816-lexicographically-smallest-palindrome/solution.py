class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                if(ord(s[i])>ord(s[j])):
                    s[i]=s[j]
                else:
                    s[j]=s[i]
                i+=1
                j-=1
        return ("").join(s)

