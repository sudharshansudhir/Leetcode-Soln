class Solution:
    def countKeyChanges(self, s: str) -> int:
        i=0
        c=0
        while i+1<len(s):
            if not s[i].lower()==s[i+1].lower():
                c+=1
            i+=1
        return c
