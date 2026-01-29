class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        c=0

        while len(grid[0])>0:
            a=[]
            for i in grid:
                m=max(i)
                a.append(m)
                i.remove(m)
            c+=max(a)
        return c


