class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind=0
        c=0
        for i in range(len(mat)):
            if mat[i].count(1)>c:
                c=mat[i].count(1)
                ind=i
        return [ind,c]
