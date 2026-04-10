class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans=[]
        t=""
        def backtrack(curr,val):
            if len(curr)==val:
                ans.append(curr)
                return 
            backtrack(curr+"0",val)
            backtrack(curr+"1",val)
            return
        backtrack("",len(nums[0]))
        for i in ans:
            if i not in nums:
                return i
        
