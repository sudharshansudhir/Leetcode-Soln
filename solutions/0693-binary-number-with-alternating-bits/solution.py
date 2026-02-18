class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=bin(n)[2:]
        i=0
        j=1
        while j<len(s):
            if s[i]==s[j]:
                return False
            i+=1
            j+=1
        return True
