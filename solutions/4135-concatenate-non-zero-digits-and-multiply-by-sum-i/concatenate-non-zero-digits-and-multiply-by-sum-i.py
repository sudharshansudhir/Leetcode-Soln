class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=[]
        s=""
        for i in str(n):
            if not i=="0":
                x.append(int(i))
                s+=i
        if(len(x)==0):
            x.append(0)
        print(sum(x))
        if(n==0):
            return 0
        return sum(x)*int(s)