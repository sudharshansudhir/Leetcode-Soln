class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            a=abs(nums[i])-1
            nums[a]=-(abs(nums[a]))
            print(nums[a])
        print(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1) 
        return res
