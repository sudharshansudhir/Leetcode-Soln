class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        n=s.count("a")
        n2=s.count("b")
        return abs(n-n2)
