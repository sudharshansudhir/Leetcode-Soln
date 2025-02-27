class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l,h=0,0
        if (not low%2==0 and not high%2==0) or (low%2==0 and not high%2==0):
            h=low//2
            l=high//2 +1
        else:
            h=low//2
            l=high//2

        return l-h
            
