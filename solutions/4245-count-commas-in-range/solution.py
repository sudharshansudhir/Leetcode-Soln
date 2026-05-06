class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        k=0
        for i in range(1000,n+1):
            k+=1
        return k
