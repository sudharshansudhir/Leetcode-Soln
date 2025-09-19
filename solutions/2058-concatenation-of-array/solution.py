class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(2):
            for j in range(len(nums)):
                n.append(nums[j])
        return n
