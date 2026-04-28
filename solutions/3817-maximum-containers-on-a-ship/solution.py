class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n=n*n
        while n*w>maxWeight:
            n=n-1
        return n
