class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans=[]
        n=len(s)
        i=0
        j=n
        for letter in s:
            if letter=="I":
                ans.append(i)
                i+=1
            else:
                ans.append(j)
                j-=1
        if i not in ans and i<len(ans):
            ans.append(i)
        else:
            ans.append(j)
        return ans
