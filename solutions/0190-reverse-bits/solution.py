class Solution:
    def reverseBits(self, n: int) -> int:
        a=format(n,'032b')
        s=str(a)
        s=s[::-1]
        aa=int(s,2)
        return aa

