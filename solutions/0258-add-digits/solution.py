class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            num=str(num)
            t=[]
            for i in num:
                t.append(int(i))
            num=sum(t)
        return num

