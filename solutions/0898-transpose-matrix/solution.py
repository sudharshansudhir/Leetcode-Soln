class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr=[]
        for i in range(len(matrix[0])):
            t=[]
            for j in range(len(matrix)):
                t.append(matrix[j][i])
            arr.append(t)
        return arr
