class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            flag=False
            for j in range(0,num+1):
                x=j|(j+1)
                if  x==num:
                    ans.append(j)
                    flag=True
                    break
            if not flag:
                ans.append(-1)
        print(ans)
        return ans
