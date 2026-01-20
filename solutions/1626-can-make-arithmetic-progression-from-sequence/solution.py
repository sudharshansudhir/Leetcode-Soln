class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=arr[0]-arr[1]
        c=1
        for i in range(1,len(arr)-1):
            if arr[i]-arr[i+1]==diff:
                c+=1
        if c+1==len(arr):
            return True
        return False

                
