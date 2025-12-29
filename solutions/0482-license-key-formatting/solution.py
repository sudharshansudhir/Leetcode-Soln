class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        t=""
        ans=[]
        for i in range(len(s)-1,-1,-1):
            if(s[i].isalnum()):
                if not(s[i].isdigit()):
                    j=s[i].upper()
                else:
                    j=s[i]
                if(len(t)<k):
                    t+=j
                if(len(t)==k):
                    ans.append(t[::-1])
                    t=""
        if(t):
            ans.append(t[::-1])
        s=("-".join(ans[::-1]))
        return s

