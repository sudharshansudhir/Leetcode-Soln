class Solution:
    def scoreOfString(self, s: str) -> int:
        sums=0
        for i in range(0,len(s)-1):
            val=ord(s[i])
            j=i+1
            val2=ord(s[j])
            if(val>val2):
                diff=val-val2
            else:
                diff=val2-val
            sums+=diff
        return sums
        
