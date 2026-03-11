class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # def sub(nums):
        res=[]
        def backtrack(curr,temp):
            res.append(temp[:])
            for i in range(curr,len(nums)):
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()

        backtrack(0,[])
        # res.sort()

        return res
        # return sub(nums)
