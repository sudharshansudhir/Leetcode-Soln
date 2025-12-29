class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=[]
        for i in range(len(s)-2):
            a=s[i:i+3]
            c=""
            for i in a:
                if i not in c:
                    c+=i
            print(c)
            if(len(c)==3):
                ans.append(a)
        
        return len(ans)

