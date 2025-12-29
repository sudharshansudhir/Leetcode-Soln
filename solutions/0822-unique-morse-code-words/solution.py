class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=[]
        for i in words:
            t=""
            for j in i:
                ind=ord(j)-97
                t+=m[ind]
            ans.append(t)
        ans=list(set(ans))
        return len(ans)


