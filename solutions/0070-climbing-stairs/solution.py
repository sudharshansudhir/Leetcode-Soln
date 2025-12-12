class Solution:
    def climbStairs(self, n: int) -> int:
        prime=[0,1]
        a=0
        b=1
        for i in range(n):
            prime.append(a+b)
            c=b
            b=a+b
            a=c
        print(prime)
        return prime[-1]
