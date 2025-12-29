class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=[]
        for i in arr:
            if arr.count(i)==1:
                c.append(i)
        if(k-1<len(c)):
            return c[k-1]
        return ""
