class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dict={}
        # nums.sort()
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]]=dict[nums[i]]+1
            elif nums[i]%2==0:
                dict[nums[i]]=1
            else:
                continue
        
        for k,v in dict.items():
            if v==1:
                return k
        return -1
            
                
        