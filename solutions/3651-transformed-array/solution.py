class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                p=nums[i]
                d=i+p
                d=d%len(nums)
                res.append(nums[d])
            elif nums[i]<0:
                 t=abs(nums[i])
                 t-=i
                 if(len(nums)<=t):
                    t%=len(nums)
                 res.append(nums[-t])
            elif nums[i]==0:
                res.append(nums[i])
        return(res)


