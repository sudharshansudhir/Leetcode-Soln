class Solution:
    def countTestedDevices(self, n: List[int]) -> int:
        c=0
        for i in range(len(n)):
            if n[i]>0:
                c+=1
                for j in range(i+1,len(n)):
                    n[j]=max(0,n[j]-1)
            else:
                continue
        return c