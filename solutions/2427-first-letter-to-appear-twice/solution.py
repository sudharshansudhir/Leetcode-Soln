class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=[]
        for i in s:
            if i in ans:
                return i
            ans.append(i)
