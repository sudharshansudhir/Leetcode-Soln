class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        con=[]
        m=0
        maxi=0
        for i in range(len(nums)):
            val=nums[i]            
            if maxi<nums[i]:
                maxi=nums[i]
            m+=(val+maxi)
            con.append(m)


        return con