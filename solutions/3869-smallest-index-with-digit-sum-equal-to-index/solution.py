class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            w=str(nums[i])
            t=[]
            for j in w:
                t.append(int(j))
            if(sum(t)==i):
                return i
            if(not t):
                if(nums[i]==i):
                    return i
        return -1
