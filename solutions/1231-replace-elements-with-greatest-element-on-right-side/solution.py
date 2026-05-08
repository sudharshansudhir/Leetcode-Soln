class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        t=arr[:]
        t.sort(reverse=True)
        k=0
        i=0
        while i<len(arr)-1:
            if t[k] in arr[i+1:]:
                ans.append(t[k])
                i+=1
            else:
                k+=1
            
        ans.append(-1)
        return ans
