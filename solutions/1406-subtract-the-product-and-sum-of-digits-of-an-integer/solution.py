class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        mul=1
        n=str(n)
        for i in n:
            i=int(i)
            mul*=i
            sums+=i
        return mul-sums
