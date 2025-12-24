class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        p=True
        n=int(bin(n)[2:])
        for i in range(2,n-1):
            b=str(int(str(n),i))
            if not(b==b[::-1]):
                return False

        return True

