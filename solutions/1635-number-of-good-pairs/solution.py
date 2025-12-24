class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        valid=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]==nums[j] and i <j ):
                    valid.append([i,j])
        print(valid)
        return len(valid)
