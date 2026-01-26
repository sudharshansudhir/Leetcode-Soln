class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        m=max(arr)
        i=0

        if(len(arr)<=2):

            return [arr]
        while i <len(arr)-1:
            if(arr[i+1]-arr[i]==m):
                ans.append([arr[i],arr[i+1]])
            elif arr[i+1]-arr[i]<m:
                m=arr[i+1]-arr[i]
                ans=[[arr[i],arr[i+1]]]
            i+=1
        return ans


