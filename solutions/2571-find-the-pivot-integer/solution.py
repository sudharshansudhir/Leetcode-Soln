class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            left=[j for j in range(1,i+1)]
            right=[j for j in range(i,n+1)]
            # print(left,right)
            if(sum(left)==sum(right)):
                return i
        return -1
