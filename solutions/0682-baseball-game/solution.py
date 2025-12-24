class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:
            if not i.isalpha() and i not in "+":
                s.append(int(i))
                print(s)
            elif i=="+":
                f=s[-1]
                fe=s[-2]
                k=f+fe
                s.append(k)
                print(s)
            elif i=="D":
                s.append(s[-1]*2)
                print(s)
            elif i=="C":
                s.pop()
                print(s)
        return sum(s)
