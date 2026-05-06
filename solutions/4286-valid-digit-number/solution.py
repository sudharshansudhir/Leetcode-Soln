class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n=str(n)
        x=str(x)
        if x in n and not n[0]==x:
            return True
        return False
