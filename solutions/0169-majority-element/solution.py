class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0

        if(1<=len(nums) and len(nums)<=5*(10**4)):
            # maxi=max(nums)
            # if(nums.count(maxi)>len(nums)//2):
            #     return maxi
            freq={}
            for i in nums:
                freq[i]=freq.get(i,0)+1
                if(freq[i]>len(nums)//2):
                    return i
            return 0

        return c
