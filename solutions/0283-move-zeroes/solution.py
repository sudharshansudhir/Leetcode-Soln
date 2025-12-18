class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        while 0 in nums:
            nums.remove(0)
        if(len(nums)<l):
            while not len(nums)==l:
                nums.append(0)
        return nums
