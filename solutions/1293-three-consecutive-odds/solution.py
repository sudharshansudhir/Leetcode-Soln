class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        flag=False
        while i-2<len(arr):
            subArr=arr[i:i+3]
            c=0
            for j in subArr:
                if j%2==1:
                    c+=1
            if(c==3):
                flag=True
            i+=1
        return flag
