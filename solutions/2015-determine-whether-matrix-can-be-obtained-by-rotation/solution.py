class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # rev=mat[::-1]
        rev=mat[:]
        while True:
            ans=[]
            d=mat[:]
            for i in range(len(d)):
                new_a=[]
                for j in range(len(d)-1,-1,-1):
                    new_a.append(d[j][i])
                ans.append(new_a)
            mat=ans[:]
            if ans==target:
                return True
            if rev==mat:
                return False

        return False
