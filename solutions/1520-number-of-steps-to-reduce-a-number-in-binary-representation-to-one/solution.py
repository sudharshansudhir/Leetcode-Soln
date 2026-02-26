class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        c=0
        while a>1:
            if a%2==1:
                a+=1
            else:
                a=a//2
            c+=1
        return c
