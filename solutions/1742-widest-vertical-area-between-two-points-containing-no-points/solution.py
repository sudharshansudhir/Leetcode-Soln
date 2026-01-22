class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ind=[]
        for i in points:
            ind.append(i[0])
        ind.sort()
        d=0
        for i in range(len(ind)-1):
            if ind[i+1]-ind[i]>d:
                d=ind[i+1]-ind[i]
        return d
