class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left=moves.count("L")
        right=moves.count("R")
        dash=moves.count("_")
        print(left,right,dash)
        # if left>right:
        #     dash*=-1
        # final=-1*left+right+dash
        return abs(left-right)+dash
            
