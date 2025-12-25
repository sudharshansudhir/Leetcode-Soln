class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=str(n)
        m=int(m[::-1])
        return abs(n-m)

