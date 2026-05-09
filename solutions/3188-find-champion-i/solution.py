class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ind=0
        maxi=0
        for i in range(len(grid)):
            if sum(grid[i])>maxi:
                maxi=sum(grid[i])
                ind=i
        return ind
