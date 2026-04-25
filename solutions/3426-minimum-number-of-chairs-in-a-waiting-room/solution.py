class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        maxi=0
        for i in s:
            if i=="E":
                c+=1
            else:
                c-=1
            # print(c)
            maxi=max(maxi,c)
        return maxi
