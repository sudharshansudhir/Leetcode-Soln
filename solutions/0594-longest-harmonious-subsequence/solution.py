class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=1
        l=0
        while right<len(nums):
            # print(nums[left:right])
            if nums[right]-nums[left]==1:
                l=max(l,right-left+1)
                right+=1
            else:
                if not nums[right]-nums[left]==0:
                    left+=1
                    # l-=1
                else:
                    right+=1
        print(l)
        return l



