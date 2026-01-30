class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num=str(num)
        a1=str(int(num[::-1]))
        a2=str(int(a1[::-1]))
        return a2==num

