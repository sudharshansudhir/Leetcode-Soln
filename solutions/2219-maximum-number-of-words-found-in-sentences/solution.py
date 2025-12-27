class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=0
        for i in sentences:
            i=i.split()
            if len(i)>l:
                l=len(i)
        return l
