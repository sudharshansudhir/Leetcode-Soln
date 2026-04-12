class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        alp="abcdefghijklmnopqrstuvwxyz"
        alp=alp[::-1]
        for word in words:
            c=0
            for w in word:
                d=ord(w)
                c+=weights[d-97]
            res=c%26
            ans+=alp[res]
        return ans

