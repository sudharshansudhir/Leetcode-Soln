class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=score[0:]
        ans=[]
        print(a,score)
        a.sort(reverse=True)
        for i in range(len(score)):
            if(score[i]==a[0]):
                ans.append("Gold Medal")
            elif(score[i]==a[1]):
                ans.append("Silver Medal")
            elif(score[i]==a[2]):
                ans.append("Bronze Medal")
            else:
                k=a.index(score[i])+1
                ans.append(str(k))
        print(ans)
        return ans
                
