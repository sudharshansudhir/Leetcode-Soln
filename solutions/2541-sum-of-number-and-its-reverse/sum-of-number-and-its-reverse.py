class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        n=num+1
        for i in range(n):
            rev=int(str(i)[::-1])
            if i+rev==num:
                return True
        return False