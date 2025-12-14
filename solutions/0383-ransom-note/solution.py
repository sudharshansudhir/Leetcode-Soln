class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=sorted(ransomNote)
        b=sorted(magazine)
        c=a[:]
        for i in c:
            if i in b:
                a.remove(i)
                b.remove(i)
        if(len(a)==0):
            return True
        print(a,b)
        # print(sorted(ransomNote),sorted(magazine))
        return False
