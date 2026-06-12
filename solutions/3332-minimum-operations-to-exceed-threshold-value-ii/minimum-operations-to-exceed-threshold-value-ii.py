import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        c=0
        heapq.heapify(nums)
        
        while nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            news=2*x+y
            heapq.heappush(nums,news)
            c+=1
        return c
