class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)
        s+=str(n*2)
        s+=str(n*3)
        c=0
        for i in range(1,10):
            if(str(i) in s):
                c+=1
        print(s)
        if(c==9 and not "0" in s and len(s)==9):
            return True
        return False
