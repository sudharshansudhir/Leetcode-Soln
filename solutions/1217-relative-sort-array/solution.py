class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind=0
        ans=[]
        arr1.sort()
        while ind<len(arr2):
            if arr2[ind] in arr1:
                ans.append(arr2[ind])
                arr1.remove(arr2[ind])
            else:
                ind+=1
        if arr1:
            for i in arr1:
                ans.append(i)
        return ans

