class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=""
        while n:
            # n,q=divmod(n-1,26)
            divi=(n-1)//26
            modu=(n-1)%26
            n=divi
            ans+=chr(modu+ord("A"))
        return ans[::-1]