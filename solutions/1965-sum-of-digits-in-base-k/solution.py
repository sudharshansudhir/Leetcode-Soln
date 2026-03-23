class Solution:
    def sumBase(self, n: int, k: int) -> int:
        a=[]
        while n>=k:
            a.append(n%k)
            n=n//k
        a.append(n)
        return sum(a)

