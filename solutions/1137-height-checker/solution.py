class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        diff=[]
        s=heights[:]
        s.sort()
        for i in range(len(heights)):
            if(not heights[i]==s[i]):
                diff.append(heights[i])
        return len(diff)



