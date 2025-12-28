class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        text=text.split()
        b=[]
        for i in brokenLetters:
            b.append(i)
        for i in text:
            broken=False
            for j in i:
                if j in b:
                    broken=True
            if(not broken):
                print(i)
                print(b)
                c+=1
        return c
