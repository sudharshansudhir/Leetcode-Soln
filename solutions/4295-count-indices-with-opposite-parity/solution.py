class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                c=0
                for j in range(i,len(nums)):
                    if not nums[j]%2==0:
                        c+=1
            else:
                c=0
                for j in range(i,len(nums)):
                    if nums[j]%2==0:
                        c+=1
            ans.append(c)
        return ans

