class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans=[]
        while nums:
            a=max(nums)
            b=min(nums)
            nums.remove(max(nums))
            if(nums):
                nums.remove(min(nums))
            an=(a+b)/2
            ans.append(float(f"{an:.1f}"))
        print(ans)
        return min(ans)
            
