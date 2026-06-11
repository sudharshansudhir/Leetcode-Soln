class Solution:
    def makeGood(self, s: str) -> str:
        n=[]

        for i in s:
            if i.isupper() and n and i.lower()==n[-1]:
                n.pop()
            elif i.islower() and n and i.upper()==n[-1]:
                n.pop()
            else:
                n.append(i)
        return "".join(n)