class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=[]
        none=[]
        for i in mat:
            c=i.count(1)
            if c==1:
                ind=i.index(1)
                if ind not in ans and ind not in none:
                    ans.append(ind)
                else:
                    if ind in ans:
                        ans.remove(ind)
                    none.append(ind)
            else:
                for index,ea in enumerate(i):
                    if ea==1:
                        none.append(index)
                        if index in ans:
                            ans.remove(index)
            
                
        # print(ans,)
        return len(ans)
                
