class Solution:
    def processStr(self, s: str) -> str:
        c=""
        for i in s:
            if i=="*" and c:
                c=c[:len(c)-1]
            
            elif i=="#":
                c+=c
            elif i=="%":
                c=c[::-1]
            elif i.isalpha():
                c+=i
        return c