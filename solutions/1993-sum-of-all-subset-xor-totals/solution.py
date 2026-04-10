class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=[]
        def backtrack(arr,curr,temp):
            if temp:
                c=0
                for j in temp:
                    c^=j

                ans.append(c)

                
            for i in range(curr,len(arr)):
                temp.append(arr[i])
                backtrack(arr,i+1,temp)
                temp.pop()
        a=backtrack(nums,0,[])
        return (sum(ans))



        if not nums:
            return 0
        c=0
        ans=[]
        for i in nums:
            c=c^i
        return c
