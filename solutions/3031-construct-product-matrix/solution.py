import sys
sys.set_int_max_str_digits(10000000)

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        s=[]
        for i in grid:
            for j in i:
                s.append(j)
        pre=1
        post=1
        res=[1]*len(s)
        for i in range(len(s)):
            res[i]=pre
            pre=(pre*s[i])%12345
        for i in range(len(s)-1,-1,-1):
            res[i]=(res[i]*post)%12345
            post=(post*s[i])%12345
        new_grid=[]
        o=0
        for i in range(len(grid)):
            t=[]
            for j in range(len(grid[0])):
                t.append(res[o])
                o+=1
            
            new_grid.append(t)
        return new_grid

        
        
