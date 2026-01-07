class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if(not i=="*"):
                ans.append(i)
            else:
                ans.pop()
        
        a="" 
        for i in ans:
            a+=i
        return a
        


