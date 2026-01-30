class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            i=str(i)
            t=[]
            for j in i:
                t.append(int(j))
            m=max(t)
            l=len(t)
            s=""
            for ii in range(l):
                s+=str(m)
            ans+=int(s)
        return ans
