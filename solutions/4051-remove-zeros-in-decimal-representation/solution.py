class Solution:
    def removeZeros(self, n: int) -> int:
        s=""
        n=str(n)
        for i in n:
            if not i=="0":
                s+=i
        return int(s)
