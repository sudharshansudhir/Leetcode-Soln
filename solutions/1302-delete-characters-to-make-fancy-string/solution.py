class Solution:
    def makeFancyString(self, s: str) -> str:
        i=0
        j=1
        k=2
        while k<len(s):
            if s[i]==s[j] and s[j]==s[k]:
                s=s[:i]+s[j:]
            else:
                i+=1
                j=i+1
                k=j+1
            # print(s)
        return s
