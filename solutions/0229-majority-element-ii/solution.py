class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        a=list(set(nums))

        limit=len(nums)//3
    
        if(len(nums)>limit and len(a)==len(nums) and not limit==0):
            return []
        
        for i in nums:
            if(nums.count(i)>limit and not i in ans):
                ans.append(i)
        return ans
