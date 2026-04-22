class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count("1")-1
        zeros=s.count("0")
        c="1"*ones
        c+=("0"*zeros)
        c+="1"
        return c

