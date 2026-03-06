class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # flag=False
        i=0
        if len(s)==1 or s=="10" or s=="11":
            return True

        # j=1
        c=0
        ans=[]
        while i<len(s):
            if s[i]=="1":
                c+=1
            else:
                if c and ans:
                    return False
                if c:
                    ans.append(c)
                    c=0
            i+=1
        if c:
            ans.append(c)
        if ans and len(ans)<2:
            return True
        return False
        

