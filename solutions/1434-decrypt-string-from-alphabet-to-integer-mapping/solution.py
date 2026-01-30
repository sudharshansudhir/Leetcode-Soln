class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        i=0
        while(i<len(s)-2):
            if(s[i+2]=="#"):
                ans.append(int(s[i:i+2]))
                i+=2
            else:
                if not s[i]=="#":
                    ans.append(int(s[i]))
                i+=1
        print(s[i:])
        if(not "#" in s[i:]):
            for ea in s[i:]:
                ans.append(int(ea))        
        elif(not "#" in s[i+1:]):
            for ea in s[i+1:]:
                ans.append(int(ea))
        print(ans)
        a=""
        for i in ans:
            a+=chr(i+96)
        return a

        
