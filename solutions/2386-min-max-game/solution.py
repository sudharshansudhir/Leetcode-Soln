class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        flag=True
        while len(nums)>1:
            i1=nums.pop(0)
            i2=nums.pop(0)
            if flag:
                nums.append(min(i1,i2))
                
            else:
                nums.append(max(i1,i2))
            flag=not flag
        return nums[0]
