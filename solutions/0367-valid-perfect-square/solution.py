class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s=int(num**0.5)
        print(s)
        if(s*s==num):
            return True
        return False
