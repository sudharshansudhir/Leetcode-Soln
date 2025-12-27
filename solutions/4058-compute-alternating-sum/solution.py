class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            if not(i%2==0):
                a.append(-abs(nums[i]))
            else:
                a.append(abs(nums[i]))
        print(a)
        return sum(a)
