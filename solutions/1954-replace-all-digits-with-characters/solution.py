class Solution:
    def replaceDigits(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isdigit():
                an=ans[-1]
                ans+=chr(ord(an)+int(i))
            else:
                ans+=i
        return ans
