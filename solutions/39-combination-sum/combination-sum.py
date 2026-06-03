class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(ind,curr):
            if sum(curr)==target:
                ans.append(curr[:])
                return
            elif sum(curr)>target:
                return
            for i in range(ind,len(candidates)):
                curr.append(candidates[i])
                backtrack(i,curr[:])
                curr.pop()
        backtrack(0,[])
        return ans
            