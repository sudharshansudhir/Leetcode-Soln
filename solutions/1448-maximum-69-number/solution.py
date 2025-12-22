class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        ans=[]
        j=0
        while j<len(s):
            t=""
            for i in range(len(s)):
                if s[i]=="6" and i==j:
                    t+="9"
                elif s[i]=="9" and i==j:
                    t+="6"
                else:
                    t+=s[i]
            ans.append(int(t))
            j+=1
        ans.append(num)
        return max(ans)
                


