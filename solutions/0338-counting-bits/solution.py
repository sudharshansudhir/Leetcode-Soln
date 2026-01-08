class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            d=str(bin(i)[2:])
            ans.append(d.count("1"))
        return ans

