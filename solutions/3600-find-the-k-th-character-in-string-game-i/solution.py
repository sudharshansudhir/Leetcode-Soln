class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<k:
            for ea in s:
                s+=chr(ord(ea)+1)
        
        return s[k-1]
