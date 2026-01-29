class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr=[]
        for i in range(len(grid)):
            for j in grid[i]:
                arr.append(j)
        s1=len(arr)
        ss=list(set(arr))
        n=max(ss)
        s2=len(arr)
        miss=0
        for i in range(1,n+1):
            if i not in ss:
                miss=i

        if miss==0:
            miss=s1
        repeat=0
        for i in arr:
            if arr.count(i)>1:
                repeat=i
                break
        return [repeat,miss]

