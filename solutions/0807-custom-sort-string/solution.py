class Solution:
    def customSortString(self, order: str, s: str) -> str:
        t=""
        s=list(s)
        i=0
        while i<len(order):
            if order[i] in s:
                t+=order[i]
                s.remove(order[i])
            else:
                i+=1
        if s:
            for i in s:
                t+=i
        return t
        

