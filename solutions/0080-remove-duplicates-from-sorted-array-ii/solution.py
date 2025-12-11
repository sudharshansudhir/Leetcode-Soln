class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        k=2
        while(k<=len(nums)-1):
            if(nums[i]==nums[j]==nums[k]):
                nums.pop(k)
            else:
                i+=1
                k+=1
                j+=1
        print(nums)
        return len(nums)
