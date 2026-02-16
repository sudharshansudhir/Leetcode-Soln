class Solution:
    def reverseBits(self, n: int) -> int:
        # n=n%32
        a=str(bin(n)[2:])
        le=len(a)
        while len(a)<32:
            a="0"+a
        # print(a)
        a=a[::-1]
        return int(a,2)
