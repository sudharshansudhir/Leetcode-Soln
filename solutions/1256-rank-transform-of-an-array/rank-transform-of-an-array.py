class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=list(set(arr[:]))
        s.sort()
        dict={}
        c=1
        for i in s:
            dict[i]=c
            c+=1
        ans=[]
        for i in arr:
            ans.append(dict[i])
        return ans