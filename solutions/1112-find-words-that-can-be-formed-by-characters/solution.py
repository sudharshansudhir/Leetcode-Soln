class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        c=[]
        for i in chars:
            c.append(i)

        for i in words:
            flag=True
            d=c[:]
            for j in i:
                if j not in d:
                    # print(j,c)
                    flag=False
                else:
                    d.remove(j)
            if flag:
                ans+=len(i)
        return ans
                    
