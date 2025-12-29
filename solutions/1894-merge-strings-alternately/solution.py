class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        l=0
        n=0
        if(len(word1)<len(word2)):
            l=len(word1)
            n=word2
        else:
            l=len(word2)
            n=word1
        for i in range(l):
            ans+=word1[i]
            ans+=word2[i]
        for i in range(l,len(n)):
            ans+=n[i]
        return ans
