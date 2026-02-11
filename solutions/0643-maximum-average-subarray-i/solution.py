class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        sub=sum(nums[i:j+1])
        l=sub/k
        j+=1
        while j<len(nums):
            sub-=nums[i]
            sub+=nums[j]
            l=max(l,sub/k)
            i+=1
            j+=1
            
        return l
