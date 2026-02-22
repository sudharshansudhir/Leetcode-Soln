class Solution:
    def binaryGap(self, n: int) -> int:
        i=0
        n=bin(n)[2:]
        print(n)
        m=0
        j=1
        while j<len(n):
            if n[i]=="0":
                i+=1
                j=i+1
            else:
                if n[j]=="1":
                    m=max(j-i,m)
                    i+=1
                    j=i+1
                else:
                    j+=1
        if m:
            return m
        return 0
