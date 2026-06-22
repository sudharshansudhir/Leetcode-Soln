class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # dum=nums[:]
        ans=[]
        for i in range(len(nums)):
            curr=nums[i]
            f=False
            dum=nums[i+1:]+nums[:i]
            for e in range(len(dum)):
                if dum[e]>curr:
                    ans.append(dum[e])
                    f=True
                    break
            if not f:
                ans.append(-1)
        return ans
            