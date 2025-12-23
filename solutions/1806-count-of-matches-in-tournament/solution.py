class Solution:
    def numberOfMatches(self, n: int) -> int:
        s=[]
        while n>1:
            a=n-(n//2)
            s.append(a)
            n=n//2
        print(sum(s))
        return sum(s)

