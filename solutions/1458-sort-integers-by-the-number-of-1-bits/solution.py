class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in arr:
            b=bin(i)[2:]
            ans.append([b.count("1"),i])
        ans.sort()
        t=[]
        for i in ans:
            t.append(i[1])
        if t==arr:
            arr.sort()
            return arr
        return t
        
