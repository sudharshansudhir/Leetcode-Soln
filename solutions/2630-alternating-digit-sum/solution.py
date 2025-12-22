class Solution:
    def alternateDigitSum(self, n: int) -> int:
        p=True
        s=str(n)
        ss=[]
        for i in s:
            if(p):
                ss.append(int(i))
                p=not p
            else:
                ss.append(-int(i))
                p=not p
        return sum(ss)
