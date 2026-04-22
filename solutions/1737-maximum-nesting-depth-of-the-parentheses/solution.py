class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxi=0
        for i in s:
            if i=="(":
                c+=1
            elif i==")":
                c-=1
            maxi=max(maxi,c)
        return maxi
