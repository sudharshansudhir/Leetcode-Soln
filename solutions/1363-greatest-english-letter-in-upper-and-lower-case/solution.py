class Solution:
    def greatestLetter(self, s: str) -> str:
        # s=str(set(list(s)))
        t=""
        m=ord("A")
        for i in s:
            if i.lower() in s and i.upper() in s and ord(i.upper())>=m:
                t=i.upper()
                m=ord(t)
        return t

