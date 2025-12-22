class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
       for i in range(1,n+1):
            s=n*i
            if(s%2==0):
                return n*i
       return n*2


