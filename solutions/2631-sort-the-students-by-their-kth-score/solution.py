class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ind=[]
        v={
        }
        c=0
        for i in score:
            ind.append(i[k])
            v[i[k]]=c
            c+=1

        ind.sort()
        ans=[]
        ind=ind[::-1]
        for i in ind:
            d=v[i]
            ans.append(score[d])
        return ans


