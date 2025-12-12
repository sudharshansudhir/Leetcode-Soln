class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=nums[0]
        og=nums[0:]
        e=nums[-1]
        ans=[]
        index=[]
        for i in range(len(nums)):
            if(nums[i] not in ans):
                ans.append(nums[i])
            else:
                index.append(nums[i])
                break
        nums.sort()
        nums.remove(index[-1])
        for i in range(len(nums)):
            if not (i+1==nums[i]):
                index.append(i+1)
                break
        if(len(index)==1):
            index.append(len(og))
        print(index)  
        return index

