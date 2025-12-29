class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        word=' '.join(words)
        print(word)
        a= word.split(separator)
        ans=[]
        for i in a:
            an=i.split()
            for j in an:
                ans.append(j)
        return ans

