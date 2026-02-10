class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            odd=set()
            even=set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
            # print(even,odd)   
                if len(odd)==len(even):
                    
                    ans=max(ans,j-i+1)
        return ans


