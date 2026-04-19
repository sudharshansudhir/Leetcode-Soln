class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = list(zip(*matrix[::-1]))
        news=[]
        for i in range(len(matrix)):
            # t=[]
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            matrix[i].reverse()
        
            # for row in matrix:
            #     row.reverse()
        # print(news)
        # matrix=news[:]

        
