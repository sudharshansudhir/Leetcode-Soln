class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        ans=[]
        dict={}
        for i in range(len(word)):
            if word[i].isupper() and word[i].lower() not in dict.keys():
                dict[word[i].lower()]=i
        print(dict)
        
        for i in range(len(word)):
            if word[i].islower() and word[i] in dict.keys():
                if i<dict[word[i]] and word[i] not in word[i+1:]:
                    c+=1
                         

        return c
