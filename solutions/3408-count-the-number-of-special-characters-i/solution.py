class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        ans=[]
        for i in word:
            if i.lower() in word and i.upper() in word and i.lower() not in ans:
                ans.append(i.lower())
                c+=1
        return c
