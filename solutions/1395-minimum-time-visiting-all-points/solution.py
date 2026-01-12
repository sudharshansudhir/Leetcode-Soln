class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        c=0
        for i in range(len(points)-1):
            a1=abs(points[i][0]-points[i+1][0])
            a2=abs(points[i][1]-points[i+1][1])
            s=max(a1,a2)
            print(s)
            ans+=s
        return ans
            
