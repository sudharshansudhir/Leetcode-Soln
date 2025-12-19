class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        if(n==1):
            return True
        i=1

        while True:
            # print(i**3,n)
            if(3**i==n):
                return True
            elif(3**i>n):
                return False
            i+=1

