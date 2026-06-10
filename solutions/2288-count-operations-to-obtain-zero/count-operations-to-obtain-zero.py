class Solution:
    def countOperations(self, n1: int, n2: int) -> int:
        c=0
        while True:
           if n1==0 or n2==0:
              return c
           if n1>n2:
              n1=n1-n2
           else:
              n2=n2-n1
           c+=1
        return c

