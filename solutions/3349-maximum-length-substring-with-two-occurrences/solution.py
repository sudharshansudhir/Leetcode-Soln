class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=0
        subarr=[]
        l=0
        for right in range(len(s)):
            subarr.append(s[right])
            while subarr.count(s[right])>2:
                subarr.pop(0)
                # left+=1
            l=max(l,len(subarr))
        return l
