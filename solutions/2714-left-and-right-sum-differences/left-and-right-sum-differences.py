class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr=[]
        i=0
        rt=[]
        lt=[]
        while i<len(nums):
            rt=nums[i+1:]
            lt=nums[:i]
            arr.append(abs(sum(rt)-sum(lt)))
            i+=1
        return arr