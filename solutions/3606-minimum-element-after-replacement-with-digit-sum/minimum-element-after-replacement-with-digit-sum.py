class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            i=str(i)
            t=0
            for e in i:
                t+=int(e)
            arr.append(t)
        return min(arr)