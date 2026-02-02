class Solution:
    def generateTheString(self, n: int) -> str:
        a="a"
        b="b"
        ans=""
        if(n%2==0):
            for i in range(n-1):
                ans+=a
            ans+=b
        else:
            for i in range(n):
                ans+=a
        return ans
