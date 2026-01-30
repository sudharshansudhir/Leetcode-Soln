class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            sub=nums[i+1:]
            d=nums[:i+1]
            f=[]
            t=[]
            for ea in sub:
                if not ea in t:
                    t.append(ea)
            for ea in d:
                if not ea in f:
                    f.append(ea)
            
            # print(f,t)
            ans.append(len(f)-len(t))
        return ans

