class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if nums==[0]:
            return 0 
        small=100000
        i=0
        while i<len(nums):
            left=max(nums[:i+1])
            rt=min(nums[i:])
            dif=(left-rt)
            if dif<=k:
                small=min(small,i)
            i+=1
        if small==100000:
            return -1
        return small

