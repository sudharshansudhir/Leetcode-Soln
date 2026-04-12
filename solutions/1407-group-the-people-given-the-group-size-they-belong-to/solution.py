class Solution:
    def groupThePeople(self, grp: List[int]) -> List[List[int]]:
        # mc=max(grp)
        ans=[]
        for i in range(1,len(grp)+1):
            t=[]
            for j in range(len(grp)):
                if i==grp[j]:
                    t.append(j)
                if len(t)==i:
                    ans.append(t)
                    t=[]
            if t:
                ans.append(t)
        ans.sort()
        return ans

