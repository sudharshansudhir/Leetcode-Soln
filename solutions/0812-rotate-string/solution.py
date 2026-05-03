class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        i=0
        while i<n:
            if s==goal:
                return True
            i+=1
            s=s[1:]+s[0]
        return False
