class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        one=s[0]
        c=0
        for i in "aeiou":
            if i in one:
                c+=one.count(i)
        for i in range(1,len(s)):
            d=0
            for e in "aeiou":
                if e in s[i]:
                    d+=s[i].count(e)
            if d==c:
                s[i]=s[i][::-1]
        return " ".join(s)