import sys
class Solution:
    def largestOddNumber(self, num: str) -> str:
        sys.set_int_max_str_digits(1000000)
        if(int(num[-1])%2==1):
            return num
        num=int(num)
        while num>=1:
            if num%2==1:
                return str(num)
            num=num//10
        return ""

