class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxv=0
        maxc=0
        for i in s:
            if i in "aeiou":
                c=s.count(i)
                if(c>maxv):
                    maxv=c
            else:
                c=s.count(i)
                if(c>maxc):
                    maxc=c
        return maxv+maxc
                
