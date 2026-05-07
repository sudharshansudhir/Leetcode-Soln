class Solution:
    def checkString(self, s: str) -> bool:
        if "b" in s:
            ind=s.index('b')
            if "a" in s[ind:]:
                return False
            # return True
        return True
