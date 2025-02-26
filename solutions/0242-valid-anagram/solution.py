class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        if len(s)!=len(t):
            return False
        for i in t:
            if t.count(i)==s.count(i):
                continue
            else:
                return False
        return True
