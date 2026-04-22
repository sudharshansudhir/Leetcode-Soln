class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i=0
        while i<len(s):
            j=len(s)-i-1
            if s[i]==s[j]:
                return i
            i+=1
        return -1
