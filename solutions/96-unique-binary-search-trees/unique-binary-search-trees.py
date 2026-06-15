from math import comb
class Solution:
    def numTrees(self, n: int) -> int:
        ncr=comb(n*2,n)
        return ncr//(n+1)