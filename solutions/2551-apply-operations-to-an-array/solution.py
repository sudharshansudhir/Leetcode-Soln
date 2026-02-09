class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        while j<len(nums):
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
            i+=1
            j+=1
        j=0
        zero=[]
        while j<len(nums):
            if nums[j]==0:
                zero.append(nums.pop(j))
            else:
                j+=1
        
            

        return nums+zero
