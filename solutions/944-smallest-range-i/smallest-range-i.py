class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        i=0
        mi=min(nums)
        mx=max(nums)
        i1=nums.index(mi)
        i2=nums.index(mx)
        while i<k:
            if mi>=mx:
                return 0
            else:
                nums[i1]=nums[i1]+1
                nums[i2]=nums[i2]-1
            # print(nums)
            i+=1
        # print(nums)
        if nums[i2]<=nums[i1]:
            return 0
        return nums[i2]-nums[i1]