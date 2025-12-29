class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        flag=False
        if(max(arr)==0):return True
        for i in range(len(arr)):
            if(arr[i]>=0):
                # print(arr[:i],arr[i+1:],i*2)
                if arr[i]*2 in (arr[:i]+arr[i+1:]):
                    return True
            elif(arr[i]<0):
                a=-arr[i]*2
                if(-a in arr):
                    return True
            
        return False
