class Solution:
    def concatenatedBinary(self, n: int) -> int:
        c=""
        for i in range(1,n+1):
            k=bin(i)[2:]
            c+=k
        # print(int(c,2))
        if int(c,2)>1000000007:
            return int(c,2)%1000000007
        return int(c,2)
