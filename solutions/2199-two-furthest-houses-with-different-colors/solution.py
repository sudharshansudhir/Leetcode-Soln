class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i=0
        j=1
        d=0
        # while i<len(colors) and j<len(colors):
        #     if not colors[i]==colors[j]:
        #         d=max(d,j-i)
        #         j+=1
        #     else:
        #         i+=1
        # print(d)
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if not colors[i]==colors[j]:
                    d=max(d,j-i)
        return (d)
