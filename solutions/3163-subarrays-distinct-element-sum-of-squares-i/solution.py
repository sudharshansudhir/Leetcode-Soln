class Solution:
    def sumCounts(self, arr: List[int]) -> int:
        c=0
        # ans=[]
        for i in range(len(arr)):
            j=0
            while j+i<len(arr):
                subarr=arr[j:j+i+1]
                c+=len(list(set(subarr)))**2
                j+=1
        print(c)
        return c
    
