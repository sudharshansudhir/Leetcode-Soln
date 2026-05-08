class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        if len(o)>m*n or len(o)<n*m:
            return []
        ans=[]
        k=0
        for i in range(m):
            kk=[]
            for j in range(n):
                kk.append(o[k])
                k+=1
            ans.append(kk[:])
        return ans
