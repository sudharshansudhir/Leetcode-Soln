class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if nums.count(i)==2 and i not in ans:
                ans.append(i)
        x=0
        for i in ans:
            x=i^x
        return x
