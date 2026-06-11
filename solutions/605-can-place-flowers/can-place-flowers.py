class Solution:
    def canPlaceFlowers(self, f: List[int], k: int) -> bool:
        c=0
        for i in range(len(f)):
            if f[i]==1:
                continue
            l=(i==0) or (f[i-1]==0)
            r=(i==len(f)-1) or (f[i+1]==0)
            if l and r:
                f[i]=1
                c+=1
        return c>=k