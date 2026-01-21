class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        k=0
        spaces.sort()
        t=""
        for i in range(len(s)):
            # print(i,spaces[k],k)
            if(i==spaces[k]):
                ans.append(t)
                t=""
                k+=1
                if(k==len(spaces)):
                    k-=1
            t+=s[i]
        if t:
            ans.append(t)
        print(ans)
        d=""
        for i in ans:
            d+=i
            d+=" "
        return d[:len(d)-1]
            


