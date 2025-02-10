class Solution:
    def clearDigits(self, s: str) -> str:
        ans=""
        c=0
        for i in range(0,len(s)):
            if(s[i].isdigit()):
                if not(len(ans)==1):
                    l=len(ans)-1
                    ans=ans[0:l]
                else:
                    ans=""
            else:
                ans+=s[i]
        return ans
           
