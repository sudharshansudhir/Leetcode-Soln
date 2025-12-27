class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        c=[]
        for i in range(len(words)):
            if x in words[i]:
                c.append(i)
        return c
