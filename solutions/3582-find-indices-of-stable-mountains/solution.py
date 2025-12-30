class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ind=[]
        for i in range(1,len(height)):
            if(height[i-1]>threshold):
                ind.append(i)
        return ind
