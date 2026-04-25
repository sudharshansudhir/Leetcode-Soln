class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx=bin(x)[2:]
        yy=bin(y)[2:]
        c=0
        if len(yy)<len(xx):
            s="0"*(len(xx)-len(yy))
            yy=s+yy
        elif len(xx)<len(yy):
            s="0"*(len(yy)-len(xx))
            xx=s+xx
        c=0
        for i in range(len(xx)):
            if xx[i]==yy[i]:
                continue
            c+=1
        return c
