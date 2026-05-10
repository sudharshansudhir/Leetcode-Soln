class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            s=bin(n)[2:]
            if "0" in s:
                n+=1
            else:
                return n
