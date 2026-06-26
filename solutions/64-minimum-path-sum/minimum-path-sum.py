class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dict={}
        def calc(r,c):
            if r>=len(grid) or c>=len(grid[0]):
                return float('inf')
            if r==len(grid)-1 and c==len(grid[0])-1:
                return grid[r][c]
            if (r,c) in dict.keys():
                return dict[(r,c)]
            first=calc(r,c+1)
            sec=calc(r+1,c)
            dict[(r,c)]=grid[r][c]+min(first,sec)
            return dict[(r,c)]
        ans=calc(0,0)
        return ans