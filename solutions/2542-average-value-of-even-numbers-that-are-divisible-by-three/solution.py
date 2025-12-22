class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            if i%3==0:
                if(i%2==0):
                    ans.append(i)
        print(ans)
        print(sum(ans),len(ans))
        if(ans):
            return (sum(ans)//len(ans))
        return 0
