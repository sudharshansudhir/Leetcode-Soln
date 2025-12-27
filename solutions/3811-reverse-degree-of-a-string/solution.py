class Solution:
    def reverseDegree(self, s: str) -> int:
        o=[]
        for i in s:
            a=ord(i)-71
            if(a==26):
                o.append(a)
            else:
                d=a-26
                o.append(26-d)

        s=[]
        print(o)
        for i in range(len(o)):
            s.append((i+1)*o[i])
        print(s)
        return sum(s)
