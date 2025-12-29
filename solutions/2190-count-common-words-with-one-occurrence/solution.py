class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # words1.extend(words2)
        ans=[]
        for i in range(len(words1)):
            if words1.count(words1[i])==1:
                ans.append(words1[i])
        an=[]
        for i in ans:
            if i in words2 and words2.count(i)==1:
                an.append(i)
        return len(an)
