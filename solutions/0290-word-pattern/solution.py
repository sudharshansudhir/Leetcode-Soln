class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if not(len(pattern)==len(s)):
            return False
        l=[]
        word=[]
        for i in range(len(pattern)):
            if pattern[i] not in l:
                l.append(pattern[i])
            if s[i] not in word:
                word.append(s[i])
        for i in range(len(s)):
            if l.index(pattern[i])!=word.index(s[i]):
                print(l.index(pattern[i]),word.index(s[i]))
                return False
        return True

