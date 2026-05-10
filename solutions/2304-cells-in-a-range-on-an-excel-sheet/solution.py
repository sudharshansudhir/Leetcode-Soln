class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s=s.split(":")
        ls=ord(s[0][0])
        le=ord(s[1][0])
        ns=int(s[0][1])
        ne=int(s[1][1])
        ans=[]
        nums=[]
        for i in range(ns,ne+1):
            nums.append(i)
        
        for i in range(ls,le+1):
            # print(i)
            d=chr(i)
            for j in nums:
                j=str(j)
                ans.append(d+j)
        return ans
