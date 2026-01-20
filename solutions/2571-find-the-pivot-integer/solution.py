class Solution:
    def pivotInteger(self, n: int) -> int:
        arr=[i for i in range(1,n+1)]
        for i in range(len(arr)):
            # print(arr[:i],arr[i:])
            first=sum(arr[:i+1])
            second=sum(arr[i:])
            if(first==second):
                return i+1
        return -1
