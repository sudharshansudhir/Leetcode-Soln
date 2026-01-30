class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            d=""
            for i in range(len(s)-1):
                ec=(int(s[i])+int(s[i+1]))%10
                d+=str(ec)
                # print(ec)
            print(d)
            s=d
        # print(s)
        if(s==s[::-1]):
            return True
        return False
