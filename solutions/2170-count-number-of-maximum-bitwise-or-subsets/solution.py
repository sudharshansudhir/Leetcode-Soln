class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans=[]
        maxor=0
        for i in nums:
            maxor=i|maxor
        
        def backtrack(curr,temp):
            if temp:
                # temp.sort()
                # if temp not in ans:
                ans.append(temp[:])
            for i in range(curr,len(nums)):
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()
        backtrack(0,[])
        # print(ans)
        c=0
        for i in ans:
            minior=0
            for j in i:
                minior=j|minior
            if minior>maxor:
                maxor=minior
        # print(maxor)
        
        for i in ans:
            minior=0
            for j in i:
                minior=j|minior
            # print(i,minior)
            if maxor==minior:
                c+=1

        return c

