class Solution:
    def minimumFlips(self, n: int) -> int:
        s=str(bin(n)[2:])
        if s==s[::-1]:
            return 0
        ss=s[::-1]
        c=0
        i=0
        while i<len(s):
            if not s[i]==ss[i]:
                c+=1
            i+=1
        print(c)
        return c

