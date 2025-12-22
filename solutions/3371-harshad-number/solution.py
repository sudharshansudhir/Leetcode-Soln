class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=[]
        ss=str(x)
        for i in ss:
            s.append(int(i))
        if(x%sum(s)==0):
            return sum(s)
        return -1

