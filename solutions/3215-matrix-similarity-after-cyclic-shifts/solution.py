class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        c=0
        temp=mat[:]
        while c<k:
            ans=[]
            for t in range(len(temp)):
                if t%2==0:
                    arr=temp[t][1:]+temp[t][:1]
                else:
                    arr=temp[t][-1:]+temp[t][:-1]
                ans.append(arr)
            print(ans)
            temp=ans[:]

            c+=1
        if ans==mat:
            return True
        
        return False


