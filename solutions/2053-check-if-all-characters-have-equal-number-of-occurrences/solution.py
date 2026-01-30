class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ini=s.count(s[0])
        for i in s:
            if not s.count(i)==ini:
                return False
        return True
