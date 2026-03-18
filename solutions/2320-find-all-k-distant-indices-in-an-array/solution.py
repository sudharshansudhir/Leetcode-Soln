class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        i,j=0,0
        arr=[]
        while j<len(nums) and i<len(nums):
            if nums[j]==key:
                d=abs(i-j)
                if d<=k:
                    arr.append(i)
                elif i>j and d>k:
                    j+=1
                    continue
                i+=1
            else:
                j+=1
        return arr


