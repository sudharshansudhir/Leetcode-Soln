class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        for i in range(len(A)):
            ar1=A[:i+1]
            ar2=B[:i+1]
            cmon=[]
            for j in ar1:
                if j in ar2:
                    cmon.append(j)
            n=len(cmon)
            ans.append(n)
        return ans
