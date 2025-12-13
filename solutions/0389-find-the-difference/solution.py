class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst=[i for i in t]
        slst=[i for i in s]

        while slst:
            if slst[0] in lst:
                lst.remove(slst[0])
                slst.remove(slst[0])
        ans=''
        for i in lst:
            ans+=i
        return ans
                 
