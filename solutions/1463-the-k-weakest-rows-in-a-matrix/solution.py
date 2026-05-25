class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[]
        for i in range(len(mat)):
            arr.append([mat[i].count(1),i])
        arr.sort()
        ans=[]
        for i in arr:
            ans.append(i[1])
        return ans[:k]

