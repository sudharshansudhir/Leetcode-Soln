class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        l=len(a[-1])
        print(a[-1])
        return l
