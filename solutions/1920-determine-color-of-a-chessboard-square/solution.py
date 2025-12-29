class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l=coordinates[0]
        d=int(coordinates[1])
        if((l in "aceg" and d%2==1)or(l in "bdfh" and d%2==0)):
            return False
        return True
