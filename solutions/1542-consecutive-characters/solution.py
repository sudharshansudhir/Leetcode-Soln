class Solution:
    def maxPower(self, s: str) -> int:
        i=0
        j=1
        c=1
        while j<len(s):
           if s[i]==s[j]:
              c=max(c,j-i+1)
              j+=1
           else:
            i+=1
            j=i+1
        return c

            
