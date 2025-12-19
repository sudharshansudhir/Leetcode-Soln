class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==1):
            return True
        i=1
        while True:
            if(4**i==n):
                return True
            elif(4**i>n):
                return False
            i+=1
