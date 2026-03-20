class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr=[["."]*n for i in range(n)]
        ans=[]
        def check(row,col):
            for r in range(row):
                if arr[r][col]=="Q":
                    return False
            r,c=row-1,col-1
            while r>=0 and c>=0:
                if arr[r][c]=="Q":
                    return False
                r-=1
                c-=1
            
            r,c=row-1,col+1
            while r>=0 and c<n:
                if arr[r][c]=="Q":
                    return False
                r-=1
                c+=1
            return True

        def backtrack(row):
            if row==n:
                ans.append(["".join(r) for r in arr])
                return
            for col in range(n):
                if check(row,col):
                    arr[row][col]="Q"
                    backtrack(row+1)
                    arr[row][col]="."
        backtrack(0)
        return ans

