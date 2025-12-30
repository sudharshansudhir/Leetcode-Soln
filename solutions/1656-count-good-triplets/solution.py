class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans=[]
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    a1=abs(arr[i]-arr[j])
                    b1=abs(arr[j]-arr[k])
                    c1=abs(arr[i]-arr[k])
                    if(a1<=a and b1<=b and c1<=c):
                        ans.append((arr[i],arr[j],arr[k]))
        return len(ans)

