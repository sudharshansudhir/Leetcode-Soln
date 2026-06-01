class Solution:
    def totalNQueens(self, n: int) -> int:
        c=0
        def isSafe(row,col):
            r=row-1
            while r>=0:
                if board[r][col]=="Q":
                    return False
                r-=1
            
            r=row-1
            c=col-1

            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            r=row-1
            c=col+1
            while r>=0 and c<n:
                if board[r][c]=="Q":

                    return False
                c+=1
                r-=1
            return True

        board=[["."]* n for i in range(n)]
        print(board)

        def check(row):
            if n==row:
                nonlocal c
                # print(c)
                c+=1
                return
            
            for col in range(n):
                if isSafe(row,col):
                    
                    board[row][col]="Q"
                    check(row+1)
                    board[row][col]="."
        check(0)
        return c
