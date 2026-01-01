class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)-1):
            if(nums[i] not in nums[i+1:] and nums[i] not in nums[:i]):
                if(nums[i] not in ans):
                    ans.append(nums[i])
        if(nums and nums[-1] not in ans and nums[-1] not in nums[:len(nums)-1]):
            ans.append(nums[-1])
        print(ans)
        if(len(ans)==2):
            return ans
        return nums
