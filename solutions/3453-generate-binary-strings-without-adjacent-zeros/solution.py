class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]

        def backtrack(pos, curr, n):
            if pos == n:
                
                ans.append(curr)
                return
         # choose 0 
            backtrack(pos + 1, curr + "0", n) # choose 1 
            backtrack(pos + 1, curr + "1", n) 
        backtrack(0, "", n)
        s=[]
        for ea in ans:
            flag=True
            for i in range(len(ea)-1):
                if ea[i]=="0" and ea[i+1]=="0":
                    flag=False
            if flag:
                s.append(ea)
        return s

        

