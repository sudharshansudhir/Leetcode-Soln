class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            mini=min(matrix[i])
            ind=matrix[i].index(mini)
            flag=True
            for j in range(len(matrix)):
                if not i==j:
                    for k in range(len(matrix[j])):
                        if(ind==k):
                            if(matrix[j][k]>mini):
                                flag=False
            if(flag):
                return [mini]
        return []
               
                    
                            


