class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr=[[0 for i in range(n)]for j in range(n)]
        print(arr)
        lst=[i for i in range(1,(n*n)+1)]
        print(arr,lst)
        top,bottom,left,right=0,n-1,0,n-1
        while top<=bottom and left<=right:
            # print()
            for i in range(left,right+1):
                arr[top][i]=lst[0]
                lst.pop(0)
            top+=1
            for i in range(top,bottom+1):
                arr[i][right]=lst[0]
                lst.pop(0)
            right-=1
            if left<=right:
                for i in range(right,left-1,-1):
                    arr[bottom][i]=lst[0]
                    lst.pop(0)
                bottom-=1
            if top<=bottom:
                for i in range(bottom,top-1,-1):
                    arr[i][left]=lst[0]
                    lst.pop(0)
                left+=1
        print(arr)
        return arr

