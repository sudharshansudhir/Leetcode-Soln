class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr=[]
        t=[]
        l=len(strs[0])
        for i in range(l):
            t=[]
            for e in strs:
                t.append(e[i])
            arr.append(t[:])
        c=0
        for i in arr:
            s=i[:]
            s.sort()
            if not s==i:
                c+=1
        return c
