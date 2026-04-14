class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                n=len(words[i])
                if words[j][:n]==words[i] and words[j][-n:]==words[i]:
                    c+=1
        return c
