class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=""
        c=""
        for i in s:
            c+=str(ord(i)-96)
        
        if(len(c)>1):
            for i in range(k):
                cc=0
                for j in c:
                    cc+=int(j)
                c=str(cc)
            return int(c)
        return int(c)


