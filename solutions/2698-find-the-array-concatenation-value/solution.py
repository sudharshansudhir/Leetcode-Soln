class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        s=[]
        # i=0
        # l=len(nums)-1:
        while nums:
            f=nums.pop(0)
            if(nums):
                l=nums.pop()
                s.append(int(str(f)+str(l)))
            else:
                s.append(f)
        if nums:
            s.append(nums[0])
        return sum(s)

