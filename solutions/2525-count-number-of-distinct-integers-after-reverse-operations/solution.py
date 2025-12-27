class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        c=0
        reve=[]
        for i in nums:
            reve.append(int(str(i)[::-1]))
        for i in reve:
            nums.append(i)
        return len(list(set(nums)))
