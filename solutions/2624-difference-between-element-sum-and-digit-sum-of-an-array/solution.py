class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        t=[]
        for i in range(len(nums)):
            te=str(nums[i])
            for j in te:
                t.append(j)
        s2=sum(map(int,t))
        print(s-s2)
        return s-s2
