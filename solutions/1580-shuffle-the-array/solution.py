class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first=nums[:n] 
        sec=nums[n:]
        m=len(nums)
        ans=[]
        j=1
        for i in range(m//2):
            ans.append(first[i])
            ans.append(sec[i])
        print(ans)
        return ans


