class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=0
        while i<len(s):
            d=s[i:]+s[:i]
            if(d==goal):
                return True
            i+=1
        return False
