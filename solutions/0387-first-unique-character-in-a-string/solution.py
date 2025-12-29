class Solution:
    def firstUniqChar(self, s: str) -> int:
        p=[]
        for i in range(len(s)):
            if s[i] not in s[i+1:]:
                if(s.count(s[i])==1):
                    return i
        return -1
