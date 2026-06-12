class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=""
        while n:
            n,q=divmod(n-1,26)
            ans+=chr(q+ord("A"))
        return ans[::-1]