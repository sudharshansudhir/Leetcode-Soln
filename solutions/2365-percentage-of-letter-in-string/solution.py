# import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=len(s)
        l=s.count(letter)
        return (l*100)//c
