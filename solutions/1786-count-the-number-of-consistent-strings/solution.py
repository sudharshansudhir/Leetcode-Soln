class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        word=[]
        for i in words:
            a=[]
            for j in i:
                a.append(j)
            word.append(a)
        for i in range(len(word)):
            t=0
            for j in range(len(word[i])):
                if word[i][j] in allowed:
                    t+=1
            if(t==len(word[i])):
                c+=1

        return c
