class Solution:
    def partitionString(self, s: str) -> int:
        ans=[]
        j=0
        t=""
        while j<len(s):
            if s[j] not in t:
                t+=s[j]
                j+=1
            else:
                ans.append(t)
                t=s[j]
                j+=1
        if(t):
            ans.append(t)
        print(ans)
        return len(ans)

            

