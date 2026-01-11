class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=""
        c=0
        r=True
        for i in range(0,len(s),k):
            if(r):
                a+=s[i:i+k][::-1]
                r=not r
            else:
                a+=s[i:i+k]
                r=not r
        print(a)
        return a


