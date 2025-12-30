class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=[]
        app=[]
        n=len(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if((i==0 and j==n-1)or(i==n-1 and j==0) or (i+j==n-1)  or(i==j)or(i==0 and j==0) or (i==n-1 and j==n-1)) and [i,j] not in app:
                    ans.append(mat[i][j])
                    app.append([i,j])
        print(ans)
        print(app)
        return sum(ans)
