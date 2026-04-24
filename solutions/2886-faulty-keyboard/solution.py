class Solution:
    def finalString(self, s: str) -> str:
        n=""
        for i in s:
            if i=="i":
                n=n[::-1]
            else:
                n+=i
        return n
