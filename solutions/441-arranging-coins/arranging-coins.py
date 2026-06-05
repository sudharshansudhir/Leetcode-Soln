class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while n>0:
            # i+=1
            if n<i:
                return i-1
            n=n-i
            i+=1
            # i+=1
            # print(i,n)
        return i-1