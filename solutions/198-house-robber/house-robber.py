class Solution:
    def rob(self, nums: List[int]) -> int:
        first=0
        sec=0
        for n in nums:
            t=max(first+n,sec)
            first=sec
            sec=t
            print(first,sec)
        return sec