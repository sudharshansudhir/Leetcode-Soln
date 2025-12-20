class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        j=i+1
        while j<len(nums):
            for ii in range(nums[i]):
                ans.append(nums[j])
            i+=2
            j+=2
        return ans
