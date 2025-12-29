class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num=num[::-1]
        for i in range(len(num)):
            if not num[i]=="0":
                a=num[i:]
                return a[::-1]
