class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans=[]
        i=1
        # mountain.sort()
        while i<len(mountain)-1:
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                ans.append(i)
            i+=1
        return ans
