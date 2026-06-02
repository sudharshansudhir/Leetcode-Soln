class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(ind,curr):
            t=curr[:]
            t.sort() 
            if curr not in ans and t not in ans:
                ans.append(t[:])
                
            for i in range(ind,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()

        backtrack(0,[])
        ans.sort()
        return ans