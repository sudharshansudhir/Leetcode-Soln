class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ss=0
        for i in range(len(s)):
            k=t.index(s[i])
            ss+=abs(i-k)
        return ss
