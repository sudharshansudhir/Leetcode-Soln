class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=nums[:]
        nums.sort()
        nums=nums[::-1]
        return nums[k-1]

        i=0
        while arr:
            m=max(arr)
            arr.remove(m)
            i+=1
            if(i==k):
                return m

