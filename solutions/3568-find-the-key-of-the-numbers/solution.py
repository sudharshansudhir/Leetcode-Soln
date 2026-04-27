class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=str(num1)
        num2=str(num2)
        num3=str(num3)
        l1=len(num1)
        l2=len(num2)
        l3=len(num3)
        s=""
        r1=4-l1
        r2=4-l2
        r3=4-l3
        n1=("0"*r1)+num1
        n2=("0"*r2)+num2
        n3=("0"*r3)+num3
        for i in range(4):
            a=[int(n1[i]),int(n2[i]),int(n3[i])]
            s+=str(min(a))
        print(s)
        return int(s)

