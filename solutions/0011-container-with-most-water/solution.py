class Solution:
    def maxArea(self, height: List[int]) -> int:
        first=0
        last=len(height)-1
        m=0
        while first<last:
            area=(last-first)*min(height[first],height[last])
            m=max(area,m)
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return m
