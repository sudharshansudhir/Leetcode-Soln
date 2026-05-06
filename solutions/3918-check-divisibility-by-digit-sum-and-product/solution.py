class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        s=0
        p=1
        for i in n:
            i=int(i)
            s+=i
            p*=i
        if int(n)%(s+p)==0:
            return True
        return False
