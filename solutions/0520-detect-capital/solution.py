class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        n=len(word)
        for i in word:
            if(65<=ord(i) and ord(i)<91):
                c+=1
        if(c==n or (c==1 and  (65<=ord(word[0]) and ord(word[0])<91)) or c==0):
            return True
        return False
            

