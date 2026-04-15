class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        flag=True
        i=0
        c=0
        while len(arr)>1:
            c+=1
            # print(arr[i],c)
            if c==k:
                arr.pop(i)
                c=0
            else:           
                i+=1
            if i>len(arr)-1:
                i=0
        return arr[0]


